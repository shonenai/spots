# MONSTER · spot corto «El primer sorbo» · v2 «con movimiento» · Seedance 2.5
*2026-10-01 · 24 s en 3 tramos de 8 s · 9:16 · 480p · 24 cr por tramo*

Por qué v2: la v1 ancló cada corte a una foto terminada y salió un pase de diapositivas. Aquí las imágenes solo fijan caras, ropa y ambiente; el movimiento lo describe el texto (acción, cámara, cambios de velocidad, golpe de música en cada corte), como en el prompt de Nike que sí funcionó. Sin Samuel, para ganar claridad.

Hilo: un sorbo desata una onda verde que lo arrastra todo, del laboratorio al desierto y al coche del jefe.
Vestuario único en toda la pieza: Sophia con sombrero pork pie + mono amarillo atado a la cintura + camiseta blanca; Enrique con mono atado a la cintura + camiseta gris.

## BLOQUE COMÚN (va al inicio de los tres tramos)
<!-- COMUN -->
REFERENCE RULES: @Image1 is the very first frame of the video. @Image2 defines the two characters and their outfits: match faces, hair and clothes exactly. Other images are STYLE and SETTING references only: copy their place, light and colour, never their pose or framing.

CHARACTER SOPHIA: 19, very fair freckled skin, long copper-red wavy hair, light eyes. Black pork pie hat in every shot, yellow chemical coverall tied at the waist, white ribbed tank top, black boots. Deadpan, in control, always one step ahead.
CHARACTER ENRIQUE: early 30s, dark curly mid-length hair, moustache and short goatee, olive skin. Yellow coverall tied at the waist, grey t-shirt, black boots. Pure joy, laughs with his whole body.

STYLE: vertical 9:16. New Mexico desert drug-lab thriller look: handheld 35mm, hard sun, warm yellow-amber grade, heavy grain, deep shadows. Neon green is the only saturated colour. Constant motion: fast cuts on the beat, whip-pans, crash zooms, speed ramps (real-time, slow-motion, real-time), the camera never rests on a tripod and no shot is a held pose. Signature shots from inside objects. Gritty distorted desert-rock guitar riff over a heavy trap beat, a hard hit on every cut. No dialogue, only laughs, shouts and breathing.

NEGATIVE: no still frames, no slideshow, no posed tableaux, no frozen characters, no on-screen text, no subtitles, no logos except the drink can, no distorted hands, no change of face between shots, no car badges.
<!-- FIN COMUN -->

## TRAMO 1 · 0:00–0:08 · «EL SORBO»
Referencias: @Image1 `fotos/A01_dentro-lata-final.png` (job ca5f5bc9) · @Image2 `fotos/A03_choque-manos.png` (job c11db16c) · @Image3 `fotos/A02_enrique-flota.png` (job 25a50afc, solo estilo y sitio)
<!-- TRAMO1 -->
[0:00 - 0:01.5] HOOK · INSIDE THE CAN
Opens on @Image1. POV from inside the can looking up. The tab cracks, daylight floods in, foam surges. SOPHIA's face fills the opening, she tips the can and the liquid rushes past the lens toward her mouth.
SFX: tab crack and fizz = first beat drop.

[0:01.5 - 0:02.5] HER EYES
SMASH CUT, crash zoom into SOPHIA's eyes under the hat brim: her irises ignite neon green, one slow blink, then she looks straight at the lens.
SFX: electric hum rising.

[0:02.5 - 0:05] THE LAB GOES WEIGHTLESS
Whip-pan off her face into the filthy motorhome lab (setting and light of @Image3). A neon green shockwave rips through the room: speed ramp to slow motion as every flask, beaker and blob of green liquid leaves the tables. ENRIQUE is lifted off the floor mid-step, arms flailing, hair rising, laughing; the handheld camera orbits half a turn around him as he tumbles in the air. Snap back to real time: everything drops, glass bounces, he lands on his feet and staggers.
SFX: sub-bass boom, glass clinking, his laugh.

[0:05 - 0:06.5] OUT THE DOOR
Without stopping, SOPHIA strides past him and kicks the motorhome door open; hard desert sun blasts in. He runs after her. The camera chases them out through the doorway, whip-pan into the open desert.
SFX: door slam on the beat, boots on metal steps.

[0:06.5 - 0:08] RUNNING HIGH FIVE
Low tracking shot, both sprinting on the dirt beside the motorhome. He catches up and they slap a high five on the run without slowing down: a neon green ring of dust bursts from their hands and races along the ground. The dust wave hits the lens and whites out the frame.
SFX: palm slap = beat hit, low whoosh.
<!-- FIN TRAMO1 -->

## TRAMO 2 · 0:08–0:16 · «EL VIAJE» (pendiente de ver el tramo 1)
Arranca en el último fotograma del tramo 1. El motorhome cruza el desierto a toda velocidad con seguimiento a ras de suelo, Enrique asomado por la trampilla del techo, salto en la duna con cámara lenta en el punto más alto y llamas verdes, aterrizaje a plomo, zoom brusco al parabrisas con Sophia conduciendo impasible y bebiendo, derrape hasta parar junto al sedán negro.

## TRAMO 3 · 0:16–0:24 · «EL JEFE Y EL CIERRE» (pendiente)
Arranca en el último fotograma del tramo 2. El jefe da su sorbo impasible; el sedán empieza a botar como un lowrider con él al volante y los gemelos rebotando tiesos; la cámara gira a ras de suelo alrededor del coche; Sophia cruza andando sin mirar; Enrique hace el mortal desde el techo del motorhome al fondo; Sophia lanza la lata a cámara, la lata gira y cae sobre negro; la garra se enciende y se apaga. Fundido y zarpazos en el montaje local (`montaje/montar.py`).
