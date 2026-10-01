---
name: competencia
description: Investiga a la competencia en Instagram/TikTok para copiar la FORMA (no el tema) de sus vídeos que mejor funcionan. Baja los reels de 5 cuentas, descarta los que no midieron, transcribe los que quedan y los desarma siempre en las mismas 6 columnas. Úsala cuando el usuario diga "COMPETENCIA", "investigar competencia", "espiar competidores", "analizar reels de X", o quiera una tabla comparativa de ganchos/formatos de otras cuentas.
---

# COMPETENCIA — análisis de forma, no de tema

Fuente: guía de Leonardo Montano · consultor de IA · [@laiasinverso](https://instagram.com/laiasinverso)
Notion: https://early-seashore-f17.notion.site/C-mo-funciona-mi-sistema-para-investigar-a-la-competencia-trigger-COMPETENCIA-3d559dec933881a58525cb1596f98ef2

El resultado siempre es el mismo: una tabla con una fila por reel, desarmada en columnas fijas, para copiar la **forma** (precio concreto en la primera frase, un número en pantalla, una idea por vídeo) y ponerla encima de nuestro tema. Nunca se copia el tema.

## Los 4 movimientos, en este orden

1. **Juntar** los últimos 30 reels de cada una de las 5 cuentas, con sus views.
2. **Descartar** los que no midieron. Se queda **solo** con los que sacaron **≥ 2× el promedio de views de esa cuenta**. Lo último que subió una cuenta puede ser justo lo que no le funcionó — por eso se filtra por rendimiento, no por fecha.
3. **Transcribir** textual solo los que quedaron.
4. **Desarmar** cada uno en estas 6 columnas exactas, aunque en algún vídeo queden vacías:
   con qué abre · qué tipo de gancho es · qué problema toca · cómo lo resuelve · qué pide al final · qué se ve en pantalla.

El paso 2 es el que casi todos se saltan y el que decide todo. El paso 4 tiene que dar **siempre** las mismas columnas: si cada semana se anota algo distinto son opiniones sueltas; si se anota siempre lo mismo, a la tercera semana se puede contar.

## Opción 1 (por defecto): programa que corre solo

### Requisitos que pone el usuario (una vez)
- Cuenta Claude Pro/Max (ya la tiene).
- API key de **scrapecreators.com** — baja los reels de cada cuenta con sus views. Tiene crédito gratis para arrancar.
- API key de **supadata.ai** — transcribe. Tiene crédito gratis para arrancar.
- Con 5 cuentas/semana el crédito gratis dura meses.

**Pídeselas al usuario tú y guárdalas en `.env`, nunca dentro del código.** Si no las ha dado, pídelas antes de escribir nada.

### Qué construir
Un script (Node o Python, el que encaje en el repo) que, dada una lista de 5 cuentas de Instagram:

1. Trae los últimos 30 reels de cada cuenta con ScrapeCreators, con sus views.
2. Se queda solo con los reels con **≥ 2× el promedio de views de su cuenta**. Los demás los descarta y no los procesa.
3. Transcribe con Supadata **solo** los que quedaron.
4. Arma una tabla, una fila por reel, con estas columnas exactas:
   `cuenta, views, primera_frase, tipo_gancho, problema, como_lo_resuelve, que_pide_al_final, que_se_ve_en_pantalla`
   - `primera_frase`: las palabras exactas de los primeros 3 segundos, **textual, palabra por palabra**. No resumir, no mejorar.
   - `tipo_gancho`: pregunta · dato · error común · promesa · contraste · otro.
   - `problema`: qué le duele al que mira, en menos de 10 palabras.
   - `que_se_ve_en_pantalla`: paso a paso · antes y después · hablando a cámara · capturas · solo texto · otro.
   - Si un dato no está: escribir **"no se ve"** y nunca completarlo por cuenta propia.
   - `cuenta` y `views` no se inventan: salen del dato de ScrapeCreators.
5. Guarda todo en `competencia.csv`, abrible en Excel. **No pisa lo de la semana pasada: agrega filas.**
6. Escribe en pantalla 3 cosas, **contando fila por fila, sin aproximar**:
   - qué primera frase se repite en más cuentas (y en cuántas exactamente),
   - qué formato no usamos ninguno,
   - qué reel sacó muchas más views que el resto de su cuenta y qué tiene distinto.

### Protocolo de ejecución
- **Antes de escribir código**: explicar en criollo qué se va a hacer y cuánto crédito consume la primera corrida. Esperar el OK.
- Las keys se piden al usuario y van a `.env` (añadir `.env` a `.gitignore`).
- **Al terminar**: dejar el `competencia.csv` y decir en **una línea** cómo se vuelve a correr la semana siguiente sin pedir nada (p. ej. `node competencia.js` o `npm run competencia`).
- Para agregar o quitar una cuenta: el usuario lo dice en castellano y se edita la lista (idealmente en `.env` o un `cuentas.txt`, no hardcodeada).

## Opción 2 (fallback manual, sin instalar nada)

Si no hay keys o el usuario quiere hacerlo a mano esta tarde:

1. Bajar **6 reels de cada cuenta — los más vistos, no los últimos** — con [cobalt.tools](https://cobalt.tools) (abierto, sin cuenta). Audio si basta con lo que dicen; vídeo si se quiere la columna de "qué se ve en pantalla". Si alguno no baja, grabación de pantalla del móvil.
2. Renombrar cada archivo con `cuenta_views.mp4` (p. ej. `estudiolopez_84000.mp4`). El archivo no trae dentro de quién es ni cuánto midió.
3. Subir de 10 en 10 a **Gemini** (es la que mira vídeo de verdad; ChatGPT saca cuadros sueltos, Claude no toma vídeo) con el prompt de tandas: pedir la tabla de 8 columnas, primera frase textual, "no se ve" si falta, sin resumen del tema, "es la tanda N de 3, todavía no saques conclusiones".
4. Juntar las 3 tablas y pedir el conteo (frase que más se repite y en cuántas cuentas, formato que no uso, vídeo que se salió de su cuenta).
5. **Verificar 3 arranques a mano**: coger 3 vídeos al azar y comprobar si la primera frase es textual o la mejoró. Si la resume, pedir de nuevo esa columna.

## Los 3 errores que arruinan el resultado

1. **Mirar lo último en vez de lo más visto** → copias justo lo que no funcionó.
2. **Copiar el tema en vez del formato** → llegas tarde y encima es de ellos. Se copia la forma, no el asunto.
3. **Dejar que la IA cuente a ojo o arregle el arranque** → los números salen de contar filas; el arranque va textual o estás copiando a la IA, no a la competencia.

**El paso que más rinde y casi nadie hace:** mirar rubros que no tienen nada que ver con el nuestro. Un formato "paso a paso mostrando las manos" es de vídeos de cocina y a un contador le sirve igual — dentro de tu rubro ese formato ya lo usa tu competencia.

**El límite:** esto junta, ordena y desarma. Qué se graba lo decide el usuario.
