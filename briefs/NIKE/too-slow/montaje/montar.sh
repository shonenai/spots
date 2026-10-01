#!/usr/bin/env bash
# Montaje "TOO SLOW" sobre el corte de Iván (nokia2.mov), sin añadir ni quitar planos.
# Encima: subtítulos nuevos tapando los viejos, flash + golpe de zoom en cortes secos,
# cápsula SHÖNEN AI y swoosh arriba, y «Look at Me Now» desde 1:38.72.
# Uso: bash montar.sh [segundo]   (con un segundo, solo saca ese fotograma para revisar)
set -e
cd "$(dirname "$0")"
python gen_subs.py >/dev/null
EDIT="../../nokia2.mov"
SONG="../../ep01-la-rival/musica/look-at-me-now.wav"
DUR=55.9167

# Cortes secos del corte de Iván (sus transiciones propias no se tocan)
CUTS="3.667 4.625 6.458 15.5 17.708 20.167 22.667 28.208 32.75 33.708 35.5 38.208 39.542 44.25 50.292"
FL="0"; ZM="1"
for c in $CUTS; do
  FL="$FL+if(between(t,$c,$c+0.12),0.5*(1-(t-$c)/0.12),0)"
  ZM="$ZM+if(between(in_time,$c,$c+0.3),0.1*pow(1-(in_time-$c)/0.3,2),0)"
done
# Ventanas de diálogo: sube la voz del clip y baja la canción
DLG="between(t,1.1,2.6)+between(t,12.8,14.1)+between(t,26.8,28.2)+between(t,29.1,30.54)+between(t,36.8,38.2)+between(t,54.9,55.92)"

VIDEO="[0:v]crop=608:1080:656:0,scale=1080:1920:flags=lanczos,fps=24,setsar=1,
  zoompan=z='$ZM':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=24,
  eq=brightness='$FL':eval=frame,subtitles=subtitulos.ass[v0];
  [1:v]scale=150:-1,format=rgba,colorchannelmixer=aa=0.92[sw];
  [2:v]scale=300:-1,format=rgba,colorchannelmixer=aa=0.9[pl];
  [v0][sw]overlay=W-w-48:92[v1];[v1][pl]overlay=48:92,format=yuv420p[v]"

if [ -n "$1" ]; then
  ffmpeg -v error -y -i "$EDIT" -i assets/swoosh.png -i assets/pill.png -filter_complex "$VIDEO" -map "[v]" \
    -ss "$1" -frames:v 1 "check_$1.png"
  exit 0
fi

ffmpeg -v error -y -i "$EDIT" -i assets/swoosh.png -i assets/pill.png -ss 98.72 -t $DUR -i "$SONG" -filter_complex "
  $VIDEO;
  [0:a]aresample=48000,aformat=channel_layouts=stereo,volume='0.22+0.9*($DLG)':eval=frame[dl];
  [3:a]aresample=48000,volume='0.95-0.55*($DLG)':eval=frame,afade=t=in:d=0.05,afade=t=out:st=$(awk "BEGIN{print $DUR-2}"):d=2[mu];
  [dl][mu]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]" \
  -map "[v]" -map "[a]" -t $DUR -c:v libx264 -crf 23 -preset slow -profile:v high -pix_fmt yuv420p \
  -c:a aac -b:a 192k -ar 48000 -movflags +faststart ../NIKE_TOO_SLOW_v3_9x16.mp4
echo "OK -> ../NIKE_TOO_SLOW_v3_9x16.mp4"
