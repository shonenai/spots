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
- [x] Brief maestro de Nike (docs + PDFs) guardado en `briefs/NIKE/brief-maestro/` y revisado: faltan idea propia, nombre/carácter de los 2 personajes, firma shönen.ai, aviso spec/IA; modelos "Consilience 2.5" y "OmniFlash" sin verificar — 2026-09-29
- [ ] Nike ep. 01 → **v5 «Cenicienta con crossover»** sobre «Look at Me Now» desde 1:38.72 (143,5 BPM medidos, ~48 cortes): `briefs/NIKE/ep01-la-rival/guion-v5-cenicienta.md`, música en `musica/` — 2026-09-29
- [x] Personajes Nike sin nombre: él de barrio, educado y competitivo; ella *girly* y rival de verdad; idea «Llega arreglada. Se va ganando.»; 7 candidatos a extras del barrio → `briefs/NIKE/personajes/personajes.md` — 2026-09-29
- [x] Spot Nike «TOO SLOW» (Seedance 2.5 480p, ~321 cr): clips en `briefs/NIKE/too-slow/clips/`, guion `NIKE_TOO_SLOW_seedance.md` — 2026-09-30
- [x] Montaje v3 `too-slow/NIKE_TOO_SLOW_v3_9x16.mp4` (25 MB) = corte de Iván `NIKE/nokia2.mov` tal cual + subtítulos encima de los verdes + flash/zoom en cortes secos + logos + «Look at Me Now» 1:38.72; se rehace con `too-slow/montaje/montar.sh` — 2026-09-30
- [x] 11 fotos de campaña «TOO SLOW» (Nano Banana, refs de personajes + outfits + Luka 5) en `too-slow/fotos/` (JPG; PNG a la papelera) — 2026-09-30
- [x] Lookbook 22 s `too-slow/NIKE_TOO_SLOW_lookbook_9x16.mp4`: 4 escenas Seedance 480p (60 cr, prompts Nexus en `too-slow/lookbook/prompts.md`) + clip Luka; se rehace con `montaje/montar_lookbook.sh` — 2026-09-30
- [ ] Web: caso Nike en `PROYECTO SHONEN.AI/WEB - ULTIMA VERSION` (Astro, se sube `dist` a mano a Cloudflare) → v0.6.6, sin publicar hasta que Iván diga
- [ ] «Ahora sí que sí» (clip 05 Luka) fuera: voz de él demasiado distinta → regenerar audio/voz si se recupera
- [x] **Monster x «Breaking Bad»** (spec, 16:9, 1:30 = 3 × 30 s de Seedance 2.5 a 480p) en `briefs/MONSTER/breaking-bad/`: guion `guion-v3.md`, referencias `referencias-imagen.md` + `refs/` (hojas sin cabeza en `refs/sin-cabeza/`, escenarios en `refs/16x9/`), fotogramas clave `fotogramas/parteN/`, prompts `seedance-parte1/2/3.md` — 2026-09-30 y 2026-10-01
- [x] Monster partes 1, 2 y 3 generadas (90 cr cada una) → `clips/parteN_v1_480p.mp4`; plano nuevo de la lata para la parte 1 (`clips/parte1_insert_17-21_v1.mp4`, 16 cr); spot entero sin etalonar `clips/MONSTER_spot_preview_v1_480p.mp4` (1:31,8) — 2026-10-01
- [x] Monster voces: Sophia y Enrique = las de Seedance en la parte 1; muestras en `voces/sophia/` (9,2 s) y `voces/enrique/` (5,5 s) — 2026-09-30
- [ ] DaVinci Resolve MCP APARCADO (2026-10-01): repo en `PROYECTOS/davinci-resolve-mcp`, bridge y entrada en `~/.claude.json` hechos; falta instalar `mcp<2` en su venv (Avast corta PyPI). Iván no quiere gastar más tiempo en esto por ahora; el montaje se hace en local con ffmpeg como en Nike
- [x] Monster spot corto «El primer sorbo» (9:16, 15 s): guion v3 con 9 planos y 11 fotos (plano 1 = cámara dentro de la lata; plano 3 = choque de manos con onda verde; plano 8 = mortal de Enrique desde el motorhome) → `briefs/MONSTER/breaking-bad/spot-corto/guion.md` — 2026-10-01
- [x] Spot corto: 11 fotos en calidad alta (GPT Image 2.5 `high` 2K, 30,25 cr) → `briefs/MONSTER/breaking-bad/spot-corto/fotos/` (+ `_hoja_de_contacto.jpg`) — 2026-10-01
- [x] Spot corto: A01 (desde dentro de la lata, abertura real) y A06 (jefe al volante) repetidas (8,25 cr); prompt de 24 s listo en `spot-corto/seedance-corto.md` (3.790 car.) — 2026-10-01
- [x] Spot corto v1 generado (Seedance 2.5, 24 s, 480p, 72 cr) → `spot-corto/clips/corto_v1_480p.mp4` y montaje con zarpazos `MONSTER_corto_v1_montaje.mp4` — 2026-10-01. **RECHAZADO por Iván: parece una sucesión de fotos**
- [x] Spot corto v2, tramo 1 de prueba (8 s, 24 cr, lanzado SIN preguntar: error mío) → `spot-corto/clips/corto_v2_tramo1_480p.mp4`; prompt con acción y cámara en `spot-corto/seedance-corto-v2.md`. Tiene movimiento continuo de verdad — 2026-10-01
- [ ] Spot corto v3 «She's a monster»: videoclip sobre Ne-Yo «Beautiful Monster» desde 3:17,5 (128 BPM medidos); 3 prompts escritos en `spot-corto/seedance-corto-v3.md`, SIN generar. Falta el sí de Iván (96 cr a 480p: 14 + 8 + 10 s; 32 s en total, por recortar). 4 fotos nuevas B01–B04 hechas (11 cr) y metidas en los prompts. Tramo 1 lanzado con permiso (14 s, 42 cr, job 9ee7f8f9-3bee-4b7c-af5e-fa97a04369e4), pendiente de descargar y revisar; tramos 2 y 3 sin lanzar. Arranque nuevo: cámara subida a la lata; ojos = solo el iris en verde eléctrico; cierre de la lata reaprovechado de la v1
- [ ] Monster postproducción en DaVinci Resolve (cuando conecte el MCP): insertar plano 17–21, tapar ~26,5 s de la parte 1 (Enrique atraviesa el sofá), acento de Enrique y palabras mal dichas, etalonaje más sombrío, rótulos de Samuel, «Pollos Shönen», logo Monster arriba a la derecha, subtítulos, sonido
- [ ] Monster: decidir 720p (210 cr por parte) o quedarse en 480p y escalar en post
- [x] GitHub: repos privados `shonenai/spots` (esta carpeta, 1 commit, sin `.env` ni `.mov`) y `shonenai/kohai_game` (`PROYECTO SHONEN.AI/JUEGO SHONEN`, solo código y documentos) preparados en local — 2026-10-01
- [ ] Iván hace el primer `git push` de los dos (inicia sesión en la ventana de GitHub) y decide si sube los 2 GB de arte del juego
- [x] Miniserie de Enrique (quarterback abusón al que se traga un juego): brief del prólogo «No era una pregunta» (2:22, 20 planos, paleta, cámara, modelos y costes comprobados) → `briefs/MINISERIE/prologo/brief.md` — 2026-10-08
- [x] Miniserie: look y dos prompts Nexus de prueba (planos 12 y 18) → `briefs/MINISERIE/prologo/look-y-prompts.md`; prompts de las 5 hojas de personajes NUEVOS (Enrique, Haru, novia, Dani, Rubén) → `briefs/MINISERIE/personajes/prompts-personajes.md` — 2026-10-08
- [x] Miniserie: página «Reparto de la Miniserie» con botón de copiar prompt completo (5 hojas reales en 16:9 + Enrique y Haru en anime 4:3) → `briefs/MINISERIE/personajes/reparto.html`, publicada en https://claude.ai/artifact/3ZZfLTgSxfNpczpqjc1utQ — 2026-10-08
- [ ] Miniserie: Iván genera las hojas por su cuenta; después, escenarios e imágenes de arranque. Pendiente: nombres, voz de Enrique y modelo (Veo 3.1 solo admite imagen de arranque y no voz de referencia; OmniFlash no está en Higgsfield)
- [x] Skills de imagen instaladas globales en `~/.claude/skills/`: `UGC_iphone` (+2 referencias), `lathxbot` (FALTA `references/LATHXBOT_KNOWLEDGE.md`), `visual-dna-forensics-engine`, `cinematic-mindshft` (enrutador + variantes directo/estricto/base) — 2026-10-08
- [x] Miniserie: escenarios (pasillo, recibidor, cuarto en 3 encuadres) y el papelito, 6 prompts con lathxbot + cinematic-mindshft, añadidos a `reparto.html` (v0.2, mismo enlace) — 2026-10-08. Siguiente: imágenes de arranque por plano (con permiso de créditos) y prompts de vídeo con Nexus
- [x] Miniserie: 20 prompts de vídeo Nexus para Kling 3.0 Omni (Frames), uno por plano, en `reparto.html` v3 (mismo enlace). Iván genera él todo. Saldo Higgsfield 2026-10-08: 14,69 cr (muy por debajo de lo esperado) — 2026-10-08
- [x] Miniserie, escena del pasillo reescrita (2026-10-08): abre sobre Haru como falso protagonista, guiño = ensō lila a rotulador dentro de la taquilla, objeto = ficha metálica de arcade (ya no papelito), novia = Sofía = Soph.ia (hojas en el proyecto de Higgsfield `c23760d7-bb88-4c22-a546-60fe513b2bb2`), voces: Kling genera y se dobla después. 28 planos con prompt de vídeo (Nexus, Kling) y, del 02 al 15, prompt de imagen de arranque → `reparto.html` v5. Faltan las imágenes de arranque de los planos 16 a 28. La frase de Haru es «Omae wa mou shindeiru» (お前はもう死んでいる), tono áspero, dramático, amenazante y de meme (planos 07 susurrada y 08 gritada)
- [x] Miniserie, nombres definitivos (2026-10-08): Noah (antes Enrique), Hiro (Haru), Dereck (Rubén), Bruno (Dani, bajito y rechoncho), Sophia. Hojas y cuarto al atardecer (E3) ya generados por Iván, guardados en `briefs/MINISERIE/generadas/`. E4 y E5 se hacen EDITANDO E3 (solo cambia la luz o el encuadre). Pendiente: recolocar los clips del cuarto (planos 18 a 28) a la distribución real: cama a la izquierda, escritorio y monitor a la derecha, ventana al fondo
- [x] Miniserie, cuarto (2026-10-08): E3 atardecer y E4 noche ya hechas; plano de arquitecto E8 hecho; E5 (contraplano desde el escritorio) elegida, solo falta quitar la puerta del fondo (`generadas/escenarios/`). Pendiente recolocar los clips del cuarto (18 a 28) a esa distribución
- [x] Miniserie, cuarto (2026-10-08): contraplano definitivo = `generadas/escenarios/E5_cuarto-contraplano_v3-silla-girada.webp` (silla de frente a la cámara, vacía). Con Noah sentado se hace editándola (ficha del plano 20). La vacía sirve también para el plano 28
- [x] Miniserie, cuarto DEFINITIVO (2026-10-08): contraplano = `generadas/escenarios/E5_cuarto-contraplano_v4-con-puerta.webp` (silla de frente, puerta abierta al fondo a la izquierda: Noah se agarra a su marco). Clips del cuarto rehechos: 18 y 19 desde E3 (puerta, atardecer), 20 y 24 a 28 desde E5, 21 a 23 planos cerrados. E4 y E9 ya no se usan
- [ ] Iván prueba las 4 skills y pasa el `LATHXBOT_KNOWLEDGE.md`
- [ ] Análisis de competencia: 5 cuentas (estudios creativos con IA y marcas de moda/producto con buen gancho)

## Después
- [ ] Episodio 1: fotos → reel → carrusel → depende de: producto + permiso de créditos
- [ ] Briefs siguientes: Corridos, Soph.ia

## Decisiones
- 2026-09-30 · VoiceStudio MCP en modo `files` (variable de usuario OMNIVOICE_MCP_OUTPUT_MODE); los WAV quedan en `AppData\Roaming\OmniVoice\outputs\`. `instruct` solo acepta rasgos de voz, no emociones; frases muy cortas de Sofi salen rotas: alargarlas
- 2026-10-01 · DaVinci Resolve MCP = `samuelgursky/davinci-resolve-mcp` (MIT, v4.8.26). Iván tiene Resolve 21.0.4 y el scripting externo responde vacío (parece la edición gratuita): hace falta el «bridge» interno del repo, que solo está confirmado hasta 21.0.x → no actualizar Resolve a 21.1. Lo instala Iván (código de terceros)
- 2026-10-01 · Fotogramas clave: a partir de ahora en calidad alta (GPT Image 2.5 `high` 2K, 2,75 cr c/u); mejor entrada, mejor vídeo
- 2026-10-01 · El distribuidor es el dueño de «Pollos Shönen» (guiño a Los Pollos Hermanos); nombre y logo se ponen en postproducción
- 2026-10-01 · CRÉDITOS: preguntar SIEMPRE antes de cada gasto, también repeticiones, pruebas e importes pequeños; una orden de rehacer no es permiso. Iván quiere ver la idea o el prompt antes de generar vídeo. Desde 2026-10-08 Iván genera él TODO (imágenes y vídeo): Claude solo escribe prompts y no llama al generador
- 2026-10-01 · Lección del spot corto v1: 9 fotos cumbre ancladas una por corte = pase de diapositivas. Las fotos quedan como campaña; el vídeo se rehace en tomas continuas
- 2026-10-01 · Cada marca tiene su identidad: no reutilizar en Monster recursos de Nike «TOO SLOW» (ojo de pez, salto sobre la cámara). Monster = mundo de la serie + planos desde dentro de los objetos + verde neón + zarpazos
- 2026-10-01 · Spot corto Monster: vertical 9:16; sin rótulo «99,1» al final (solo logo en fundido); el distribuidor se desmadra en el sedán negro botando como lowrider; Sophia y Enrique son la cara de la marca y salen más
- 2026-10-08 · Miniserie: personajes nuevos (no los souls de Enrique y Sophia), fotos generadas por Iván; formato 16:9 (propuesta: mundo real a 16:9 y mundo del juego recortado a 4:3). Paradigma: en el juego los «nerds» son los fuertes
- 2026-10-01 · Clips de captación (23–25 s) = muy dinámicos y sobre canción; vídeos largos = ritmo tranquilo con algo más de cámara lenta (también en `README.md`). En el spot corto la carrera va con la cámara siguiéndolos, giro orbital y cambio de foco; sin choque de manos de lado
- 2026-10-01 · GitHub: cuenta `shonenai`; commits con el correo noreply de la cuenta; memoria de Claude copiada a `docs/memoria/` para trabajar en la nube
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
