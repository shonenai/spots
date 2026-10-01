#!/usr/bin/env bash
# Lookbook "TOO SLOW" (~22 s): escenas de lookbook/ + "Ahora sí que sí" (clip 05) + tarjeta final.
# Uso: bash montar_lookbook.sh
set -e
cd "$(dirname "$0")"
python gen_subs.py lookbook
LB="../lookbook"
LUKA="../clips/05_luka_ahora_si.mp4"
SONG="../../ep01-la-rival/musica/look-at-me-now.wav"
END=1.5
TOTAL=21.915
V="scale=1080:1920:flags=lanczos,fps=24,setsar=1,format=yuv420p"
A="aresample=48000,aformat=channel_layouts=stereo"

# Tramos: mate de ella | Luka (suela + frase) | crossover | moto (sin el primer plano de ella) | final estudio
seg(){ echo "[$1:v]trim=$2:$3,setpts=PTS-STARTPTS,$V[v$4];[$1:a]atrim=$2:$3,asetpts=PTS-STARTPTS,$A[a$4];"; }
F="$(seg 0 0.25 5.05 0)$(seg 1 1.0 2.0 1)$(seg 1 3.3 5.05 2)$(seg 2 0.2 5.05 3)$(seg 3 0 0.875 4)$(seg 3 2.958 5.05 5)$(seg 4 0 5.05 6)"
F="$F[5:v]scale=1080:1920,$V,fade=in:st=0:d=0.2[v7];[6:a]$A[a7];"
F="$F[v0][a0][v1][a1][v2][a2][v3][a3][v4][a4][v5][a5][v6][a6][v7][a7]concat=n=8:v=1:a=1[vb][ab]"

CUTS="1.125 2.458 4.8 5.8 7.55 8.767 10.517 12.4 13.275 15.365 17.407 19.073 20.415"
FL="0"; ZM="1"
for c in $CUTS; do
  FL="$FL+if(between(t,$c,$c+0.12),0.5*(1-(t-$c)/0.12),0)"
  ZM="$ZM+if(between(in_time,$c,$c+0.3),0.1*pow(1-(in_time-$c)/0.3,2),0)"
done
DLG="between(t,3.4,4.85)+between(t,6.6,7.6)+between(t,19.3,20.42)"

ffmpeg -v error -y -i "$LB/s1_mate_ella.mp4" -i "$LUKA" -i "$LB/s2_crossover.mp4" -i "$LB/s3_moto.mp4" -i "$LB/s4_final.mp4" \
  -loop 1 -t $END -i assets/endcard.png -f lavfi -t $END -i anullsrc=r=48000:cl=stereo \
  -i assets/swoosh.png -i assets/pill.png -ss 98.72 -t $TOTAL -i "$SONG" -filter_complex "
  $F;
  [vb]zoompan=z='$ZM':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=24,
      eq=brightness='$FL':eval=frame,subtitles=subtitulos_lookbook.ass[v0x];
  [7:v]scale=150:-1,format=rgba,colorchannelmixer=aa=0.92[sw];
  [8:v]scale=300:-1,format=rgba,colorchannelmixer=aa=0.9[pl];
  [v0x][sw]overlay=W-w-48:92:enable='lt(t,20.415)'[v1x];[v1x][pl]overlay=48:92:enable='lt(t,20.415)',format=yuv420p[v];
  [ab]volume='0.25+0.85*($DLG)':eval=frame[dl];
  [9:a]$A,volume='0.95-0.5*($DLG)':eval=frame,afade=t=in:d=0.05,afade=t=out:st=$(awk "BEGIN{print $TOTAL-1.8}"):d=1.8[mu];
  [dl][mu]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]" \
  -map "[v]" -map "[a]" -t $TOTAL -c:v libx264 -crf 21 -preset slow -profile:v high -pix_fmt yuv420p \
  -c:a aac -b:a 192k -ar 48000 -movflags +faststart ../NIKE_TOO_SLOW_lookbook_9x16.mp4
echo "OK -> ../NIKE_TOO_SLOW_lookbook_9x16.mp4"
