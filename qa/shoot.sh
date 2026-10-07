#!/bin/bash
# usage: qa/shoot.sh <width> <pageheight> <tag>   -> qa/<tag>-<width>-<n>.png tiles of 12000px
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
W=$1; H=$2; TAG=$3; T=12000; n=0
cd "$(dirname "$0")"; cp _shot.html ../docs/_shot.html; trap "rm -f ../docs/_shot.html" EXIT
for ((y=0; y<H; y+=T)); do
  hh=$(( H-y < T ? H-y : T ))
  "$CH" --headless=new --disable-gpu --hide-scrollbars --force-prefers-reduced-motion --window-size=$W,$hh --virtual-time-budget=6000 --screenshot="$TAG-$W-$n.png" "http://localhost:4210/_shot.html?w=$W&h=$H&y=$y" 2>/dev/null
  n=$((n+1))
done
ls "$TAG-$W-"*.png
