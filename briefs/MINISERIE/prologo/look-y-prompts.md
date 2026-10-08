# Prólogo «No era una pregunta» · look y prompts Nexus
*2026-10-08 · complementa a `brief.md` · sin generar nada*

## Qué se ha sacado de cada skill
| Skill | Qué aporta aquí | Qué no aplica |
|---|---|---|
| **Nexus** | Formato de los prompts: bloque de personaje, contexto, ficha técnica, plano con posiciones medibles, sonido físico. Actuación escrita como conducta, vida en los ojos, física con peso | Nada; es la base |
| **Taste** | Decidir el look antes de generar; una familia principal y un solo acento; un color de acento por plano; generar varias y quedarse con pocas; objeto solo sobre negro como plano firma | Su paleta de ejemplo (ángeles, dorado, 138 BPM) es de otro proyecto |
| **Brag + HyperFrames** | Los textos de pantalla y los rótulos se hacen en local con HyperFrames. Regla de lectura: entra rápido y se queda quieto, unos 0,3 s por palabra | Brag monta un vídeo de lanzamiento a partir del código de una web; para ficción no sirve tal cual |
| **TasteForge** | Mantener separados «cómo se ve» y «qué pasa» | Su motor mide vídeos de referencia; solo tiene sentido si Iván trae referencias |
| **ui-ux-pro-max** | No está instalada en esta sesión | - |

## Look cerrado (regla de Taste: una familia y un acento)
- **Familia principal:** drama juvenil realista. Cine de 35 mm, grano fino, piel con poro, luz con una sola fuente clara por plano.
- **Único acento:** el juego. Cian eléctrico con núcleo blanco y textura de píxel grueso (8 bits) en los bordes de la luz.
- **Un acento por plano:** si hay cian en el plano, no hay ningún otro color saturado.
- **Plano firma (objeto sobre negro):** el papelito solo, centrado, sobre fondo casi negro. Sale tres veces: en el suelo (05), en la mano (09) y brillando en la mesa (13).
- **Un detalle de mundo por escenario**, siempre el mismo:
  - Pasillo: una pancarta pintada a mano, granate y crema, con un toro embistiendo, colgada de lado a lado.
  - Recibidor: una escalera ancha con una sola lámpara encendida al fondo.
  - Cuarto: una vitrina de cristal con un balón de fútbol americano firmado, encima del escritorio.

## Textos de pantalla (HyperFrames, en montaje)
| Plano | Texto | Palabras | Mínimo quieto |
|---|---|---|---|
| 01 | «12 horas antes» | 3 | 0,9 s |
| 11 | «0 resultados» | 2 | 0,8 s |
| 14 | «¿Cansado de tu vida? ¿Te gustaría cambiarla?» | 7 | 2,1 s |
| 17 | «En realidad no era una pregunta, Enrique.» | 7 | 2,1 s |

Estilo: tipografía de píxel, blanco sobre negro con halo cian, cursor que parpadea. Se escribe letra a letra y se queda quieto. En el plano 17 el nombre «Enrique» aparece el último, tras una pausa.

## Prompts Nexus de los dos planos de prueba
Cada uno es una toma continua de 8 s con su imagen de arranque (`@Image1`). Diálogo en español de España.

### Plano 12 · se ríe de sí mismo
<!-- P12 -->
@ENRIQUE - Already image referenced in @Image1. Voice: "A 22-year-old from Madrid, native Castilian Spanish. Warm chest voice, quick and cocky; under pressure the pitch climbs and the words get shorter." Voice only.
@CARD - a small paper ticket the size of a cinema ticket lying flat at the left edge of the desk, 10 centimeters from the keyboard, unlit and ordinary. Prop only.

SCENE: Vertical 9:16, 8 seconds, one continuous take, real time. Night, ENRIQUE's bedroom. He sits alone at his desk, centered in frame, chest 40 centimeters from the desk edge, body and eyes facing the monitor, which is just below the lens and out of frame. Behind his left shoulder, 2 meters back, a wall-mounted glass case holds a signed football that catches the monitor light. He has searched for an hour and found nothing. The room stays intact and the light stays constant. The take ends with him looking away to frame right, bored, the card untouched.

TECH: 35mm film, fine grain, medium portrait lens, shallow focus on his eyes, natural skin texture with pores. Camera locked off just above the monitor with a 10 centimeter push-in across the whole take. Lighting lock: the monitor is the key, cold blue, from below and in front; one weak warm desk lamp from camera right, behind him, as a rim on his jaw. No fill, no beauty light, the far wall falls to black. No on-screen text. Everything has weight: the chair flexes and creaks when he leans.

CUT - medium close-up @ENRIQUE centered, real time - his right hand works the mouse, eyes scanning left to right in small jumps, blinking rarely, jaw set. The scrolling stops. His hand leaves the mouse and hangs in the air: the search is over. He breathes out through his nose, a half laugh, drops back into the chair until it creaks, laces both hands behind his head and looks up at the ceiling, grinning at his own stupidity. He says to nobody: "¿Pero qué hago yo buscando esto? Si es que soy un friki." He shakes his head once, the grin fading into a yawn, and his eyes drift off to frame right, away from the desk, a slow relaxed blink - at the left edge of the desk the card lies still in shadow -

*SOUND: computer fan, mouse wheel ticks that stop, one breath through the nose, office chair creak, his voice close and dry in a small room, distant traffic through a closed window.*
<!-- FIN P12 -->

### Plano 18 · la luz lo agarra
<!-- P18 -->
@ENRIQUE - Already image referenced in @Image1. Voice: "A 22-year-old from Madrid, native Castilian Spanish. Warm chest voice, quick and cocky; under pressure the pitch climbs and the words get shorter." Voice only.
@LIGHT - a rope of liquid light as thick as a forearm, electric cyan with a white core, its edges breaking into coarse square pixels, pouring out of the monitor screen. It moves like water under pressure and pulls like a winch. Creature appearance only.

SCENE: Vertical 9:16, 8 seconds, one continuous take, real time. Night, ENRIQUE's bedroom. The monitor glows on the desk against the far wall, frame left background, 4 meters from the lens. The open door frame fills the right foreground, 50 centimeters from the lens. ENRIQUE stands midground center, 2 meters from the desk and 1.5 meters from the door frame, body turned toward the monitor, face in three-quarter profile to camera. He has just read the message and understood it. The light takes him and he catches the door frame. The take ends with him stretched horizontal between the door frame and the screen, still holding on.

TECH: 35mm film, fine grain, wide environmental lens, handheld at chest height from just outside the doorway, the horizon tilted 10 degrees. Lighting lock: the monitor is the only strong source and it is behind him, so he is backlit: his face stays in shadow with a hard cyan rim on cheek, shoulder and arm; one weak warm desk lamp at frame right gives the door frame its edge. No frontal fill. Cyan is the only saturated colour. No on-screen text. Physics lock: he weighs 90 kilos and the pull is stronger; his trainers drag and squeak on the floor before they leave it; cloth and hair lag behind his body; paper and posters fly toward the screen, heavy furniture only shudders.

CUT - wide low angle @ENRIQUE midground center, @LIGHT from the monitor at frame left, door frame at frame right, real time - he takes one step back toward the door, eyes locked on the screen, not blinking, right hand reaching behind him for the frame. @LIGHT bursts out of the screen, crosses the 2 meters in a blink and coils twice around his waist. It yanks. His trainers skid, his body folds at the hips, his feet leave the floor and he goes horizontal at waist height, twisting in the air. Both hands slam onto the door frame at frame right, 50 centimeters from the lens, knuckles whitening, fingertips sliding 5 centimeters along the painted wood. Posters rip off the wall behind him, loose papers and a pillow fly past him into the screen, the desk chair rolls and tips. He looks straight into the lens, eyes wide, pupils tiny in the cyan, and screams: "¡No, no, no!" - behind him the screen is a white rectangle swallowing everything that reaches it -

*SOUND: a deep electrical surge, trainers squealing on laminate, fabric snapping tight, two palms slapping wood, fingernails scraping paint, paper tearing, a chair hitting the floor, wind rushing inward, his voice breaking on the third "no".*
<!-- FIN P18 -->

## Qué falta para poder probarlos
- Imagen de arranque de cada plano (GPT Image 2.5, 2,75 cr cada una), que a su vez necesita la hoja de Enrique con la chaqueta y el cuarto de noche.
- Decidir el modelo de la prueba: Veo 3.1 Lite (12 cr por plano) o Seedance 2.5 (24 cr, con su muestra de voz).
- Aviso: el Enrique que tenemos aparenta unos 30 años, con bigote y perilla. Para un quarterback universitario habría que decidir si se queda así (repetidor, veterano) o se le rejuvenece en la hoja nueva.
