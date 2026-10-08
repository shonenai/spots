---
name: prompts-en-pagina-copiable
description: "Cuando Iván va a generar él las imágenes, los prompts se entregan en una página artefacto con botón de copiar (personaje + estilo + grid), como el Bestiario de Kōhai"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 4db748f8-8779-4c9c-9c47-43349b167e13
  modified: 2026-10-08T01:03:34.892Z
---

Cuando Iván genera las imágenes por su cuenta, no quiere los prompts sueltos en el chat ni en un `.md`: quiere una página artefacto donde cada ficha tenga un botón que copia el prompt ENTERO ya ensamblado (personaje + bloque de estilo + bloque del grid), con casilla de «hecho» guardada en el navegador y filtros.

**Why:** lo pidió el 2026-10-08 para la miniserie («sería una buena manera así de hacer todo de ahora en adelante»), tomando como modelo el artefacto «Bestiario de Kōhai» (https://claude.ai/artifact/6iQ5f8aCQ38KAHwaHGkUkX). Copiar y pegar tres bloques a mano le hace perder tiempo.

**How to apply:** para cualquier tanda de prompts que vaya a lanzar él (personajes, escenarios, objetos, imágenes de arranque), hacer o ampliar la página del proyecto en vez de listar prompts en el chat. Página de la miniserie: `briefs/MINISERIE/personajes/reparto.html`, publicada en https://claude.ai/artifact/3ZZfLTgSxfNpczpqjc1utQ; datos en la lista `CHARS` y bloques en `STYLE` y `GRID`; añadir una entrada y republicar el mismo fichero. No leer entero el Bestiario para copiar el patrón (pesa 200 KB): el patrón ya está en `reparto.html`. Relacionado: [[creditos-preguntar-siempre]].
