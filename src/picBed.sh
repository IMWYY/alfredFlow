#!/bin/bash
t=$(date +%s)
cp '{query}' /Users/Mark.W/Documents/AboutMyself/picBed/Screenshot${t}.png
cd /Users/Mark.W/Documents/AboutMyself/ 
git add . > /dev/null
git commit -m add_upload_picture_${t} > /dev/null
git push origin master > /dev/null
echo http://raw.githubusercontent.com/IMWYY/AboutMyself/master/picBed/Screenshot${t}.png