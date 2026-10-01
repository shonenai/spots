# shonen-briefs · roadmap
*Actualizado: 2026-10-01*

## Objetivo
Trabajar por briefs para shönen.ai: campañas, producto, vídeo e imagen para redes (TikTok, Reels, carruseles) y, según haga falta, bots, webs, concept art, impresión 3D o minijuegos.

## Dónde está cada cosa
- `briefs/NN-nombre/` — un brief por carpeta (`brief.md` + material + exports)
- `competencia/` — análisis de ganchos y formatos (skill `competencia`)
- Otros proyectos: `..\video-ugc\ROADMAP.md`, `Desktop\PROYECTO SHONEN.AI\` (juego Kōhai, web, cuento)
- Logo v2.1: `..\video-ugc\assets\brand\v2.1\`

## Hecho
- [x] Proyecto creado + brief 01 propuesto (`briefs/NIKE/01-del-movil-al-cartel/brief.md`) — 2026-09-28

## Ahora
- [x] Brief 01 aprobado; producto del ep. 1: Nike Air More Uptempo "France" (spec) → `briefs/NIKE/01-del-movil-al-cartel/ep01-uptempo-france/brief.md` — 2026-09-28
- [x] Charro calza Jordan Luka (negro/plata/rojo): prompts de foto 6 y 7 y Seedance actualizados — 2026-09-28
- [ ] Iván genera las fotos 1 y 4 en Higgsfield
- [x] Brief maestro de Nike (docs + PDFs) guardado en `briefs/NIKE/brief-maestro/` y revisado: faltan idea propia, nombre/carácter de los 2 personajes, firma shönen.ai, aviso spec/IA; modelos "Consilience 2.5" y "OmniFlash" sin verificar — 2026-09-29
- [ ] Nike ep. 01 → **v5 «Cenicienta con crossover»** sobre «Look at Me Now» desde 1:38.72 (143,5 BPM medidos, ~48 cortes): `briefs/NIKE/ep01-la-rival/guion-v5-cenicienta.md`, música en `musica/` — 2026-09-29
- [ ] (antes) Nike ep. 01 → v4 de ritmo (~40 cortes, ojo de pez, texto palabra a palabra, 5 clips de Seedance con varios planos + montaje local): `briefs/NIKE/ep01-la-rival/tratamiento-v4-ritmo.md` — 2026-09-29
- [ ] (antes) Nike ep. 01 «La motorista» (v3, 23 s, 9:16, moto naranja + tacones, voces en Seedance; guion en `briefs/NIKE/ep01-la-rival/tratamiento-v3-moto.md`). Ep. 02 = versión Uptempo con el conjunto marrón. Iván genera con el manual: Iván sigue el manual de prompts (https://claude.ai/artifact/55uuEjhDCtMeY9dtEWKRx4, fuente `briefs/NIKE/ep01-la-rival/seguimiento.html`) → 2 hojas con outfit + escenario + 6 fotogramas; luego Seedance y montaje local — 2026-09-29
- [x] Personajes Nike sin nombre: él de barrio, educado y competitivo; ella *girly* y rival de verdad; idea «Llega arreglada. Se va ganando.»; 7 candidatos a extras del barrio → `briefs/NIKE/personajes/personajes.md` — 2026-09-29
- [x] Spot Nike «TOO SLOW» (Seedance 2.5 480p, ~321 cr): clips en `briefs/NIKE/too-slow/clips/`, guion `NIKE_TOO_SLOW_seedance.md` — 2026-09-30
- [x] Montaje v3 `too-slow/NIKE_TOO_SLOW_v3_9x16.mp4` (25 MB) = corte de Iván `NIKE/nokia2.mov` tal cual + subtítulos encima de los verdes + flash/zoom en cortes secos + logos + «Look at Me Now» 1:38.72; se rehace con `too-slow/montaje/montar.sh` — 2026-09-30
- [ ] Iván revisa la v3 (tiempos de subtítulos y volumen de voces)
- [x] 11 fotos de campaña «TOO SLOW» (Nano Banana, refs de personajes + outfits + Luka 5) en `too-slow/fotos/` (JPG; PNG a la papelera) — 2026-09-30
- [x] Lookbook 22 s `too-slow/NIKE_TOO_SLOW_lookbook_9x16.mp4`: 4 escenas Seedance 480p (60 cr, prompts Nexus en `too-slow/lookbook/prompts.md`) + clip Luka; se rehace con `montaje/montar_lookbook.sh` — 2026-09-30
- [ ] Web: caso Nike en `PROYECTO SHONEN.AI/WEB - ULTIMA VERSION` (Astro, se sube `dist` a mano a Cloudflare) → v0.6.6, sin publicar hasta que Iván diga
- [ ] «Ahora sí que sí» (clip 05 Luka) fuera: voz de él demasiado distinta → regenerar audio/voz si se recupera
- [x] **Monster x «Breaking Bad»** (spec, 16:9, 1:30 = 3 × 30 s de Seedance 2.5 a 480p) en `briefs/MONSTER/breaking-bad/`: guion `guion-v3.md`, referencias `referencias-imagen.md` + `refs/` (hojas sin cabeza en `refs/sin-cabeza/`, escenarios en `refs/16x9/`), fotogramas clave `fotogramas/parteN/`, prompts `seedance-parte1/2/3.md` — 2026-09-30 y 2026-10-01
- [x] Monster partes 1, 2 y 3 generadas (90 cr cada una) → `clips/parteN_v1_480p.mp4`; plano nuevo de la lata para la parte 1 (`clips/parte1_insert_17-21_v1.mp4`, 16 cr); spot entero sin etalonar `clips/MONSTER_spot_preview_v1_480p.mp4` (1:31,8) — 2026-10-01
- [x] Monster voces: Sophia y Enrique = las de Seedance en la parte 1; muestras en `voces/sophia/` (9,2 s) y `voces/enrique/` (5,5 s) — 2026-09-30
- [ ] Iván revisa la parte 3 y el spot entero (diálogos de Samuel y del distribuidor sin comprobar: no hay transcripción)
- [ ] DaVinci Resolve MCP APARCADO (2026-10-01): repo en `PROYECTOS/davinci-resolve-mcp`, bridge y entrada en `~/.claude.json` hechos; falta instalar `mcp<2` en su venv (Avast corta PyPI). Iván no quiere gastar más tiempo en esto por ahora; el montaje se hace en local con ffmpeg como en Nike
- [ ] Monster spot corto «alocado» (estilo Nike TOO SLOW): propuesto 2026-10-01, pendiente de OK de Iván al concepto y al formato
- [ ] Monster postproducción en DaVinci Resolve (cuando conecte el MCP): insertar plano 17–21, tapar ~26,5 s de la parte 1 (Enrique atraviesa el sofá), acento de Enrique y palabras mal dichas, etalonaje más sombrío, rótulos de Samuel, «Pollos Shönen», logo Monster arriba a la derecha, subtítulos, sonido
- [ ] Monster: decidir 720p (210 cr por parte) o quedarse en 480p y escalar en post
- [ ] GitHub: decidir repo privado para trabajar en la nube (ver Decisiones)
- [ ] Análisis de competencia: 5 cuentas (estudios creativos con IA y marcas de moda/producto con buen gancho)

## Después
- [ ] Episodio 1: fotos → reel → carrusel → depende de: producto + permiso de créditos
- [ ] Briefs siguientes: Corridos, Soph.ia

## Decisiones
- 2026-09-30 · VoiceStudio MCP en modo `files` (variable de usuario OMNIVOICE_MCP_OUTPUT_MODE); los WAV quedan en `AppData\Roaming\OmniVoice\outputs\`. `instruct` solo acepta rasgos de voz, no emociones; frases muy cortas de Sofi salen rotas: alargarlas
- 2026-10-01 · DaVinci Resolve MCP = `samuelgursky/davinci-resolve-mcp` (MIT, v4.8.26). Iván tiene Resolve 21.0.4 y el scripting externo responde vacío (parece la edición gratuita): hace falta el «bridge» interno del repo, que solo está confirmado hasta 21.0.x → no actualizar Resolve a 21.1. Lo instala Iván (código de terceros)
- 2026-10-01 · Fotogramas clave: a partir de ahora en calidad alta (GPT Image 2.5 `high` 2K, 2,75 cr c/u); mejor entrada, mejor vídeo
- 2026-10-01 · El distribuidor es el dueño de «Pollos Shönen» (guiño a Los Pollos Hermanos); nombre y logo se ponen en postproducción
- 2026-10-01 · GitHub: esta carpeta no es repo, no hay `gh` ni identidad de git configurada; pendiente de decidir repo privado (sin `.env` ni vídeos pesados)
- 2026-09-30 · Voz de Enrique = la de Seedance en la parte 1 (no la de Iván), a Iván le hace gracia
- 2026-09-30 · Voz de Sophia = la que sacó Seedance en la parte 1 (a Iván le encanta); no se usa el clon de Fish
- 2026-09-30 · Monster pasa a HORIZONTAL 16:9 (en 9:16 el laboratorio se veía estrecho). Laboratorio nuevo más amplio y sucio, estilo la serie; fotogramas y escenarios se rehacen en 16:9
- 2026-09-30 · Monster: sin garras; el logo nace de 3 dedos de Enrique en la condensación de la lata. Abogado = «Samuel» («¡Mejor llama a Samuel!»). Trato en el desierto, no en el restaurante
- 2026-09-30 · Monster: nada de caras de actores reales (Saul, etc.); arquetipos originales con guiños de la serie
- 2026-09-30 · Montajes de Iván: no añadir ni quitar planos; los subtítulos nuevos tapan los viejos (nada de blur)
- 2026-09-30 · Skill `nexus-skill` (PJ Accetturo) instalada global en `~/.claude/skills/` para prompts de escena/CUT list de vídeo
- 2026-09-29 · Nike ep. 01 pasa a «Cenicienta con crossover» (cambio de outfit en cada bote) sobre «Look at Me Now»; frase fija de ella: «TOO. SLOW. PAPITO.»
- 2026-09-29 · Nike: vídeos de branding en 4:3 dentro de 9:16 con franjas negras; UGC en 9:16 a pantalla completa (tiene que parecer grabado con el móvil)
- 2026-09-28 · Proyecto separado de video-ugc para no mezclar
- 2026-09-28 · Foco de momento en redes (TikTok/Reels/carruseles); menos contenido de samuráis
- 2026-09-28 · Claves de scrapecreators y supadata en `.env` (fuera de git), con tope de créditos por corrida; avisar antes de pasarse
- 2026-09-28 · Skill `competencia` copiada a `.claude/skills/` de este proyecto
- 2026-09-28 · Voces en local con VoiceStudio (app Windows v0.5.6, instalador en Descargas); también para japonés y Soph.ia

## Pendiente de Iván
- Sí/no al brief 01 y foto de móvil del producto
- Cuentas de competencia que quieras incluir (o las elijo yo)
