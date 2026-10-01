# Genera subtítulos .ass: frase entera; la palabra que suena va en el color de la escena y un poco más grande.
# Detrás, contorno tinta grueso + franja que une las palabras (tapa texto quemado debajo).
from PIL import ImageFont

_IMPACT = 'C:/Windows/Fonts/impact.ttf'

C = {'azul': '&HFFB27F&', 'turq': '&HE6D83F&', 'oro': '&H41A4D9&', 'naranja': '&H136AFF&',
     'lila': '&HD4A4B8&', 'amarillo': '&H00E5FF&', 'rojo': '&H462DFF&'}


def band_width(text, fs):
    # libass mide \fs como alto de celda (ascent+descent); Impact: 2498/2048 em
    font = ImageFont.truetype(_IMPACT, max(1, round(fs / 1.22)))
    return int(font.getlength(text) + 2 * len(text))


def ts(t):
    return f"{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}"


def build(lines, y, path):
    """lines: [(inicio frase, fin, color, tamaño, [(palabra, inicio)])]"""
    out = [
        "[Script Info]", "ScriptType: v4.00+", "PlayResX: 1080", "PlayResY: 1920", "WrapStyle: 2",
        "ScaledBorderAndShadow: yes", "",
        "[V4+ Styles]",
        "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, "
        "Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, "
        "MarginL, MarginR, MarginV, Encoding",
        "Style: Pop,Impact,110,&H00FFFFFF,&H00FFFFFF,&H001C1216,&H661C1216,0,0,0,0,100,100,2,0,1,10,6,5,40,40,0,1",
        "",
        "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text",
    ]
    for st, en, col, fs, words in lines:
        segs = [(st, words[0][1], None)] if words[0][1] > st + 0.01 else []
        for i, (_, t) in enumerate(words):
            segs.append((t, words[i + 1][1] if i + 1 < len(words) else en, i))
        for k, (a, b, act) in enumerate(segs):
            head = "{\\an5\\pos(540,%d)\\fs%d" % (y, fs)
            if k == 0:
                head += "\\fscx125\\fscy125\\t(0,110,\\fscx100\\fscy100)"
            head += "}"
            parts, under = [], []
            for i, (w, _) in enumerate(words):
                if i == act:
                    parts.append("{\\c%s\\fscx112\\fscy112}%s{\\c&HFFFFFF&\\fscx100\\fscy100}" % (C[col], w))
                    under.append("{\\fscx112\\fscy112}%s{\\fscx100\\fscy100}" % w)
                else:
                    parts.append(w)
                    under.append(w)
            under_head = head[:-1] + "\\bord22\\shad0\\1a&HFF&\\3c&H1C1216&}"
            out.append(f"Dialogue: 1,{ts(a)},{ts(b)},Pop,,0,0,0,,{under_head}{' '.join(under)}")
            out.append(f"Dialogue: 2,{ts(a)},{ts(b)},Pop,,0,0,0,,{head}{' '.join(parts)}")
            w = band_width(' '.join(x for x, _ in words), fs) - 40
            h = int(fs * 0.5)
            draw = "{\\an5\\pos(540,%d)\\bord0\\shad0\\1c&H1C1216&\\p1}m 0 0 l %d 0 l %d %d l 0 %d{\\p0}" % (
                y, w, w, h, h)
            out.append(f"Dialogue: 0,{ts(a)},{ts(b)},Pop,,0,0,0,,{draw}")
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')


# Spot v3 (nokia2.mov): centro de los subtítulos verdes viejos
SPOT = [
    (1.25, 2.60, 'azul', 100, [('¿TÚ', 1.25), ('ESTÁS', 1.50), ('LISTO,', 1.80), ('PAPI?', 2.05)]),
    (12.60, 14.10, 'turq', 118, [('TOO', 12.95), ('SLOW...', 13.30), ('PAPITO.', 13.60)]),
    (26.85, 28.20, 'oro', 118, [('TOO', 26.90), ('SLOW...', 27.20), ('PAPITO.', 27.60)]),
    (29.20, 30.54, 'naranja', 104, [('¡VALE, VALE!', 29.20), ('¡REVANCHA!', 29.85)]),
    (36.90, 38.20, 'lila', 118, [('TOO', 36.95), ('SLOW...', 37.20), ('MAMI.', 37.55)]),
    (54.95, 55.92, 'amarillo', 124, [("LET'S", 55.00), ('DO', 55.20), ('IT!', 55.35)]),
]

# Lookbook 20 s (montar_lookbook.sh)
LOOKBOOK = [
    (3.50, 4.80, 'oro', 118, [('TOO', 3.55), ('SLOW...', 3.70), ('PAPITO.', 4.15)]),
    (6.75, 7.55, 'rojo', 112, [('AHORA', 6.80), ('SÍ', 7.00), ('QUE', 7.12), ('SÍ.', 7.22)]),
    (19.40, 20.41, 'amarillo', 124, [("LET'S", 19.45), ('DO', 19.70), ('IT!', 19.86)]),
]

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'lookbook':
        build(LOOKBOOK, 1480, 'subtitulos_lookbook.ass')
    else:
        build(SPOT, 1606, 'subtitulos.ass')
