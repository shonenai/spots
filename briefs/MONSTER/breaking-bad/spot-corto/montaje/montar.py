"""Montaje del spot corto de Monster: zarpazos verdes en cada corte + fundido final.

Uso:  python montaje/montar.py   (desde la carpeta spot-corto)
Entrada: clips/corto_v1_480p.mp4   Salida: clips/MONSTER_corto_v1_montaje.mp4
"""
import math
import os
import random
import shutil
import subprocess

from PIL import Image, ImageDraw, ImageFilter

ENTRADA = "clips/corto_v1_480p.mp4"
SALIDA = "clips/MONSTER_corto_v1_montaje.mp4"
TMP = "montaje/_tmp"
W, H, FPS = 1080, 1920, 24
DURACION = 24.064
# Cortes detectados en el clip (segundos). El de 0,54 s (oscuro -> luz) no lleva zarpazo.
CORTES = [4.125, 7.708, 9.583, 12.583, 14.917, 17.792, 19.458, 21.875]
VERDE = (149, 214, 0)        # verde Monster
NUCLEO = (235, 255, 190)     # centro casi blanco
N_FRAMES_ZARPAZO = 9         # 0,375 s; el corte cae en el fotograma 4
FUNDIDO = 0.6


def garra(progreso, alfa):
    """Tres zarpazos diagonales. progreso 0-1 = cuánto han recorrido; alfa 0-1."""
    capa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    rnd = random.Random(7)
    for i in (-1, 0, 1):
        x0, y0 = W * 0.86 + i * 250, -H * 0.04 + abs(i) * 90
        x1, y1 = W * 0.10 + i * 250, H * 1.02 - abs(i) * 60
        pasos = 60
        izq, der = [], []
        for s in range(pasos + 1):
            t = s / pasos
            if t > progreso:
                break
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            grosor = 62 * math.sin(math.pi * min(t / max(progreso, 0.01), 1.0)) ** 0.7
            grosor *= 0.75 + 0.5 * rnd.random()          # borde irregular, como un rasguño
            dx, dy = (y1 - y0), -(x1 - x0)
            n = math.hypot(dx, dy)
            dx, dy = dx / n, dy / n
            izq.append((x + dx * grosor, y + dy * grosor))
            der.append((x - dx * grosor, y - dy * grosor))
        if len(izq) > 2:
            poligono = izq + der[::-1]
            d.polygon(poligono, fill=VERDE + (255,))
            # núcleo claro: el mismo trazo estrechado hacia su eje
            n_izq = [((a + c) / 2 + (a - c) * 0.17, (b + e) / 2 + (b - e) * 0.17)
                     for (a, b), (c, e) in zip(izq, der)]
            n_der = [((a + c) / 2 - (a - c) * 0.17, (b + e) / 2 - (b - e) * 0.17)
                     for (a, b), (c, e) in zip(izq, der)]
            d.polygon(n_izq + n_der[::-1], fill=NUCLEO + (255,))
    brillo = capa.filter(ImageFilter.GaussianBlur(26))
    salida = Image.alpha_composite(brillo, capa)
    if alfa < 1:
        salida.putalpha(salida.getchannel("A").point(lambda v: int(v * alfa)))
    return salida


def fotograma_zarpazo(k):
    if k < 4:                                   # entra rasgando
        return garra((k + 1) / 4, 1.0)
    if k == 4:                                  # el corte: garra entera + destello verde
        base = garra(1.0, 1.0)
        destello = Image.new("RGBA", (W, H), VERDE + (70,))
        return Image.alpha_composite(destello, base)
    return garra(1.0, 1.0 - (k - 4) / 5)        # se apaga


def main():
    shutil.rmtree(TMP, ignore_errors=True)
    os.makedirs(TMP)
    total = int(round(DURACION * FPS))
    vacio = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    vacio.save(f"{TMP}/vacio.png")
    zarpazos = []
    for k in range(N_FRAMES_ZARPAZO):
        ruta = f"{TMP}/z{k}.png"
        fotograma_zarpazo(k).save(ruta)
        zarpazos.append(ruta)
    inicio = {int(round(c * FPS)) - 4: True for c in CORTES}
    mapa = {}
    for f0 in inicio:
        for k in range(N_FRAMES_ZARPAZO):
            mapa[f0 + k] = zarpazos[k]
    for f in range(total):
        shutil.copyfile(mapa.get(f, f"{TMP}/vacio.png"), f"{TMP}/o{f:04d}.png")

    # Sonido de zarpazo: ruido filtrado con ataque rápido, uno por corte
    retardos = "".join(
        f"[1:a]adelay={int((c - 0.12) * 1000)}:all=1[w{i}];" for i, c in enumerate(CORTES))
    mezcla = "".join(f"[w{i}]" for i in range(len(CORTES)))
    filtro = (
        f"[0:v]scale={W}:{H}:flags=lanczos,fps={FPS},setsar=1[v0];"
        f"[2:v]format=rgba[ov];[v0][ov]overlay=0:0:format=auto,"
        f"fade=t=out:st={DURACION - FUNDIDO}:d={FUNDIDO}[v];"
        f"{retardos}"
        f"[0:a]aresample=48000,volume=1.0[a0];"
        f"[a0]{mezcla}amix=inputs={len(CORTES) + 1}:normalize=0:duration=first,"
        f"afade=t=out:st={DURACION - FUNDIDO}:d={FUNDIDO}[a]"
    )
    orden = [
        "ffmpeg", "-loglevel", "error", "-y",
        "-i", ENTRADA,
        "-f", "lavfi", "-i",
        "anoisesrc=d=0.38:c=pink:a=0.9:r=48000,highpass=f=900,lowpass=f=7000,"
        "afade=t=in:d=0.04,afade=t=out:st=0.10:d=0.28,volume=0.8",
        "-framerate", str(FPS), "-i", f"{TMP}/o%04d.png",
        "-filter_complex", filtro, "-map", "[v]", "-map", "[a]",
        "-c:v", "libx264", "-crf", "17", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-t", str(DURACION), SALIDA,
    ]
    subprocess.run(orden, check=True)
    shutil.rmtree(TMP, ignore_errors=True)
    print("hecho:", SALIDA)


if __name__ == "__main__":
    main()
