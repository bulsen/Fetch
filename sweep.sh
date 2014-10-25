#!/bin/bash

# feeder ve converter'ı silip converterı slides'larda yeniden adlandırmak için yazıyorsun

cowsay "this is the fetch check for new slides please paste your slidefiles to the slides/ directory"

export LC_ALL=C
# these segments searchs .ppts and .pptxs in slides folder
# then rename with a random name and covert to required formats that we are in need to
for file in $(find slides/ -type f -name '*.ppt');
do
new_name = $(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 8 | head -n 1)
mv $file $new_name.ppt
libreoffice --headless --invisible --convert-to pptx $new_name.pptx
done

cowsay -s "I've done the pptx conversions. Now strating fetch conversions "

# now starting to converting into fetch things
# this'll route the pptxs to the fetch_converter.py and convert them into 
for pptxs in $(find slides/ -type f -name '*.pptx');
do
python fetch_converter.py $pptxs
done
