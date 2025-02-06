#!/bin/bash

file=$1
basename=$(basename "$file")
num=0
params="-c:v libx264rgb -c:a copy -max_muxing_queue_size 1024 -crf 0 -preset veryslow -y"

mkdir -p vids/pngs

# create actual clip
ffmpeg -i "$file" $params vids/temp.mkv > /dev/null 2>&1

params="-c:v libx264rgb -an -r 60 -max_muxing_queue_size 1024 -crf 0 -preset veryslow -y"

# create social clip to share by cropping the video
ffmpeg -i vids/temp.mkv -vf "scale=240:-1" $params vids/temp2.mkv > /dev/null 2>&1

# create gif of this clip
ffmpeg -i vids/temp2.mkv -vf "fps=40" vids/pngs/%04d.png > /dev/null 2>&1
gifski -r 40 -Q 100 vids/pngs/*.png -o vids/${basename%.*}.gif > /dev/null 2>&1

# clear temporary pngs
rm -rf "vids/pngs"
rm -f "vids/temp.mkv"
rm -f "vids/temp2.mkv"
