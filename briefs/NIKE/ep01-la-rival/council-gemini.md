# Council · Gemini (gemini-3.5-flash-lite) · 2026-09-29

¡Hola! Qué gran proyecto tenéis entre manos. El concepto visual (pista colorista, contraste de la chica arreglada/uñas burdeos con el entorno, y el clímax del tablero) es muy potente para Reels/TikTok. 

Vamos directos al grano con vuestras cuatro preguntas técnicas, basadas en el estado actual de las herramientas de vídeo generativo:

---

### 1) ¿Formato 4:3 con franjas (letterboxing/pillarboxing) o 9:16 a pantalla completa para retener en los 2 primeros segundos?
* **Respuesta:** **9:16 a pantalla completa, sin duda.**
* **Por qué:** En TikTok y Reels, el 9:16 es el estándar nativo. Las franjas negras ("letterboxing") actúan como barrera visual, reducen el tamaño real del contenido en el móvil y gritan "esto no es nativo". Para retener en los primeros 2 segundos (el gancho), necesitáis que la acción (ella haciendo el cruce o mirando a cámara) ocupe todo el espacio vertical. Además, la estética de bloques de color saturados de vuestra pista gana muchísimo a pantalla completa.

### 2) ¿12 clips cortos (3-5 s) o 5-6 clips más largos? (Considerando créditos, consistencia y deformaciones)
* **Respuesta:** **12 clips cortos (3-5 s) con un solo movimiento de cámara por clip.**
* **Por qué:** La IA de vídeo sufre degradación cuanto más dura un plano (aparición de extremidades extra, pérdida de detalles en las zapatillas o desfiguración facial). 
    * **Consistencia:** Al ser planos cortos, la IA "olvida" menos los detalles clave (uñas burdeos, diseño de las zapas).
    * **Control:** Te permite elegir la mejor toma de 3 opciones y descartar las que fallen.
    * **Coste/Riesgo:** Aunque consuma más créditos generar 12 clips, el coste de reintentar un plano largo de 8 segundos arruinado en el segundo 6 es mucho mayor en tiempo y frustración. El ritmo dinámico de un anuncio de 20s lo pide a gritos el montaje (cortes cada 1.5 - 2.5 segundos).

### 3) ¿Un solo clip continuo de 15s con prompts por marcas de tiempo, o clips por partes (un plano por fotograma)?
* **Respuesta:** **Clips por partes (un clip independiente por plano, usando el fotograma de Nano Banana Pro como *Image-to-Video* o *First Frame*).**
* **Por qué:** *(No lo habéis probado, os lo confirmamos por experiencia en producción).* Los prompts con marcas de tiempo en un solo clip largo **fallan frecuentemente** en modelos actuales para cambios drásticos de ángulo o acción (pasar de un plano medio a un *bullet time* cenital). La mejor forma de mantener la fidelidad de la cara y las zapatillas distintas es usar vuestros fotogramas de Nano Banana Pro como referencia de inicio (*start image*) para cada uno de los 12 clips. Así forzas al modelo a arrancar con la coherencia exacta de vestimenta, peinado y producto.

### 4) Para el mate con ruptura de tablero y *bullet time* 360°, ¿qué modelo usar y qué trucos de prompt?
* **Respuesta:** Ningún modelo actual (ni Seedance, ni Kling, ni Veo, ni Wan) os va a resolver **de forma limpia y realista** una rotura de cristal compleja combinada con un giro de 360 grados en un solo prompt automático. Es el talón de Aquiles de la IA actual.
    * **Qué modelo elegir:** **Kling 1.5/2.0 o Luma Dream Machine** suelen gestionar mejor la física de partículas y las acciones violentas (como romper cristales) que Seedance, o bien **Wan 2.1** si tenéis capacidad de computación local/API por su excelente realismo físico.
    * **Trucos de prompt (en inglés, funcionan mejor):**
        1. *Divide la acción:* No pidas el mate y la rotura a la vez. Haz un plano del salto/mate y otro plano diferente para el impacto en el cristal.
        2. *Usa términos técnicos de cámara:* *"360-degree bullet time effect, extreme slow motion, time freeze, glass shards exploding in vibrant neon colors towards the camera, hyper-realistic, dynamic action shot"*
        3. *El truco de postproducción (Pro-tip):* Generad el fondo de la pista y el salto de ella por un lado, y para los cristales rotos de colores, usad un elemento de archivo (*stock footage*) de cristales explotando en chroma o superpuestos en modo *Screen/Add* en vuestro montaje local. La IA os dará la jugadora; los efectos especiales "tradicionales" (o capas de partículas) os darán el acabado profesional sin fallos de lógica visual.