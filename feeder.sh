#!/bin/bash

for fyles in $(find slaytlar/ -type f -name '*.pptx')
do
python converter.py $fyles
done
