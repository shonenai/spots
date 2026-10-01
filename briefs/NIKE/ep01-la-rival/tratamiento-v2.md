# Ep. 01 «La rival» · tratamiento v2 — color y ritmo
*2026-09-29 · borrador a la espera de las referencias de cámara de Iván*

## La idea
Mismo duelo, otra energía: brillante, rápido, sin un plano quieto. Termina con **ella machacando y rompiendo el tablero**, que estalla en cristales de colores.

## Reglas visuales
- **Color por bloques:** cada corte cambia el color dominante, sacado de los outfits: rojo, verde, caramelo, lila, azul cielo y el dorado de las Uptempo.
- **Cancha pintada a bloques de colores**, como las canchas de barrio intervenidas por artistas, con la valla metálica alrededor.
- **Ningún plano dura más de 1,5 s**, salvo el tiempo congelado del mate.
- **Cámaras variadas:** ojo de pez a ras de suelo, cenital con dron, balón-cámara, barrido rápido, cámara lenta que acelera de golpe y vuelta de 360° congelada.
- **Firma shönen.ai: marca de agua** (`../assets/marca-agua-pill.svg`): cápsula oscura con la Ö samurái y «SHÖNEN AI», como en el vídeo de Corridos. Esquina inferior derecha, pequeña y semitransparente, durante todo el vídeo. Nada de tajos de katana.

## Guion (20 s · imagen 4:3 dentro de 9:16 con franjas negras · 120 bpm)
| s | Plano | Cámara | Color |
|---|---|---|---|
| 0-1 | Uñas burdeos aprietan los cordones de las Uptempo | macro, flash | rojo |
| 1-2 | Su zapatilla pisa la cancha pintada | ojo de pez a ras de suelo | dorado |
| 2-3 | Él gira el balón en un dedo y sonríe de lado; ella se muerde el labio y sonríe | barrido rápido hasta él | lila |
| 3-5 | Los dos en la cancha, el balón bota | cenital con dron, acelera | multicolor |
| 5-6 | Regate entre las piernas | balón-cámara | verde |
| 6-8 | Cruce en cámara lenta que acelera de golpe; él pierde el equilibrio | lateral bajo | caramelo |
| 8-9 | Los del barrio gritan agarrados a la valla | cámara en mano, temblor | azul |
| 9-10 | Ella corre hacia el aro | travelling a ras de suelo | rojo |
| 10-12 | Despega y el tiempo se congela | vuelta de 360° | todo |
| 12-13 | **MATE: el tablero estalla** en cristales de colores | contrapicado | todo |
| 13-15 | Aterriza bajo la lluvia de cristales, se coloca el pelo y **lanza un beso a cámara** | cámara lenta | dorado |
| 15-17 | Él, en el suelo, se ríe; ella le **guiña un ojo**, le tiende la mano y lo levanta | plano medio | lila |
| 17-20 | Congelado + «Llega arreglada. Se va ganando.» + «Spec · IA» | montaje | negro |

## Cámara por plano (ejes de Visual213: X lateral · Y vertical · Z profundidad)
Una sola dirección de cámara por clip: si se piden dos, la IA las mezcla y marea mal.
| Plano | Prompt de cámara (inglés) | Eje |
|---|---|---|
| 1 cordones | `extreme close-up, slow dolly in` | Z |
| 2 zapatilla | `fisheye lens at ground level, fast tracking forward` | Z |
| 3 él | `fast whip pan right landing on him` | X (panorámica) |
| 4 dron | `overhead top-down shot, crane up fast, speed ramp` | Y |
| 5 regate | `POV ball-cam, first-person from the basketball` | — |
| 6 cruce | `lateral tracking left to right, slow motion ramping to real speed` | X |
| 7 valla | `handheld close tracking, shaky, snap focus` | — |
| 8 carrera | `low tracking shot moving backward in front of her` | Z (atrás) |
| 9 despegue | `360-degree orbit around her, frozen time, bullet time` | órbita |
| 10 mate | `extreme low angle, tilt up, crash zoom in on the rim` | Y + zoom |
| 11 aterrizaje | `slow dolly out, shards falling in slow motion` | Z (atrás) |
| 12 la mano | `tilt down from her to him on the floor` | Y |

## Bloques de realismo (de las keywords de Notion; pegar al final de cada prompt)
**Piel** (siempre):
`visible pores, fine skin texture, subtle freckles, uneven skin tone, slight oil sheen, sweat microbeads, peach fuzz, fine hair strands, realistic specular highlights, subdermal translucency`

**Ropa** (siempre):
`soft fabric folds, uneven wrinkles, textile grain, fine fibers visible, cloth weight realism, fabric compression marks, natural fabric sheen`

**Cristal del tablero** (solo planos 10-11):
`real glass distortion, subtle refraction, light scattering, chromatic dispersion, micro reflections, uneven reflection`

**Cancha y valla** (planos abiertos):
`paint chipping, surface grain noise, metal oxidation on the fence, environmental dust, matte vs gloss contrast`

**Cámara** (todos): `motion blur realism, lens flare streaks, backlight bloom, cinematic color grading, subtle chromatic aberration`

❌ **No usar en este vídeo:** `desaturated realism`, `low contrast film look`, `moody highlights`, `overcast lighting`. Van contra lo brillante y colorido.
No pegar las 25 palabras de cada lista: con 6-10 basta, y más diluyen el prompt.

## Producción
- **Un clip de 3-5 s por plano** (Seedance o Kling), unos 12 en total. De cada uno aprovechamos el mejor segundo.
- **El mareo sale del montaje, no de la IA.** Aceleraciones y frenadas, destellos de color, barridos por bloques de color y diseño de sonido, todo en local con HyperFrames y sin créditos.
- **Fotos de inicio solo para 5 planos**, en los que la cara o la zapatilla tienen que salir fieles: 1, 3, 6, 12 y 15. El resto puede partir de texto con referencias.
- **Créditos:** pedir el coste antes de generar.
