---
name: metodo-video-seedance-anclas
description: Flujo que funcionó para vídeo con Seedance 2.5 en Higgsfield (spot Monster) y trampas de las herramientas que no están en el repo
metadata:
  node_type: memory
  type: project
  originSessionId: 4db748f8-8779-4c9c-9c47-43349b167e13
  modified: 2026-10-01T08:55:26.840Z
---

Flujo validado por Iván en el spot Monster x «Breaking Bad» (30-09 y 01-10-2026): guion por partes de 30 s → referencias (hojas de personaje con Soul 2.0, escenarios) → 4-5 fotogramas clave por parte con GPT Image 2.5 (hoja + escenario + producto) → Seedance 2.5 `omni_reference` con hojas sin cabeza + fotogramas como anclas (`@Image1…`) + muestra de voz como `audio_references` (`@Audio1`) → si falla un trozo, capturar fotogramas del propio clip y regenerar solo ese trozo corto.

**Why:** viene del hilo de PJ Ace (skill Nexus). Lanzar Seedance solo con hojas sobre fondo gris obligaba al modelo a inventar la composición; con fotogramas ancla las tres partes salieron bien a la primera.

**How to apply:**
- Soul 2.0 con una imagen de referencia la copia tal cual (no pone persona ni cambia escena): para combinar cara + producto + escenario usar GPT Image 2.5.
- Soul 2.0 mete texto inventado en carteles, cortinas y latas, y a veces marcos de tira de película: pedir «sin texto» y revisar siempre.
- Las hojas de personaje van «sin cabeza» en el panel de cuerpo entero (recuadro gris), como en Nike.
- Seedance 2.5: 3 cr/s a 480p (30 s = 90 cr), 7 cr/s a 720p. Higgsfield sugiere un preset al lanzar; rechazarlo con `declined_preset_id`.
- Las subidas a Higgsfield (`media_upload`) necesitan la cabecera `If-None-Match: *` en el PUT; el audio se sube como MP3.
- Prompt con el tope de 4.000 caracteres de la skill Nexus; con 8 cortes en 30 s cada corte queda en 200-300 caracteres.
- Iván quiere fotogramas en calidad alta: [[fotogramas-clave-calidad-alta]].
- Formato del spot Monster: horizontal 16:9. Voces de Sophia y Enrique = las que sacó Seedance en la parte 1.
