#!/bin/bash
TMPFILE=`tempfile`
wget "$2" -O $TMPFILE
unzip -o  $TMPFILE -d ../RetroPie/roms/$1
rm $TMPFILE
