#!/bin/bash

id=$1

if [ -f $(pwd)/trytodecrypt_$id.split ]; then
   cp $(pwd)/trytodecrypt_$id.split $(pwd)/trytodecrypt_$id-edited.split
else
   echo $2 | sed 's/\(.........\)/\1\n/g' > $(pwd)/trytodecrypt_$id.split
   cp $(pwd)/trytodecrypt_$id.split $(pwd)/trytodecrypt_$id-edited.split
fi

if [ ! -d $(pwd)/trytodecrypt_$id ]; then
   mkdir $(pwd)/trytodecrypt_$id
fi

index=0

for c in {{0..9},{a..z},{A..Z},_,-,?,!,.}; do
   if [ ! -f $(pwd)/trytodecrypt_$id/$index.char ]; then
      str=$(printf -- "$c%.0s" {1..50})
      curl "http://api.trytodecrypt.com/encrypt?key=95dc64bedb5451dde3ab8bb9b36a3431&id=$id&text=$str" | sed 's/\(.........\)/\1\n/g' > $(pwd)/trytodecrypt_$id/$index.char
   fi
   cat $(pwd)/trytodecrypt_$id/$index.char | while read line; do
      if $(grep -Fq $line $(pwd)/trytodecrypt_$id-edited.split); then
         sed -i "s/$line/$line  $c/g" $(pwd)/trytodecrypt_$id-edited.split
      fi
   done
   index=$(($index+1))
done
