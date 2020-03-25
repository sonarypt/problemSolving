#!/bin/bash

id=$1

main_folder=$(pwd)/trytodecrypt_$id

# check if editing file exists and move to decryptable format
if [ ! -f $(pwd)/trytodecrypt_$id.split ]; then
   echo $2 | sed 's/\(....\)/\1 \n/g' | sed 's/\(..\)/\1 /g' > $(pwd)/trytodecrypt_$id.split
fi

# calculate decimal value of the difference then output to the edited file
num_row=$(cat $(pwd)/trytodecrypt_$id.split | wc -l)
for i in $(seq 1 $num_row); do
   hxn=$(cat $(pwd)/trytodecrypt_$id.split | head -n$i | tail -n1 | awk '{print $1}')
   hxo=$(cat $(pwd)/trytodecrypt_$id.split | head -n$i | tail -n1 | awk '{print $2}')
   printf "$((0x$hxo - 0x$hxn))" >> $(pwd)/trytodecrypt_$id-edited.split
   printf "\n" >> $(pwd)/trytodecrypt_$id-edited.split
done

cp $(pwd)/trytodecrypt_$id-edited.split $(pwd)/trytodecrypt_$id-decrypted.split

# replace the decimal value of the difference with alphabetical characters
index=0
for c in {{0..9},{a..z},{A..Z},-,_,.}; do
   if $(grep -Fwq $index $(pwd)/trytodecrypt_$id-decrypted.split); then
      sed -i "s/$index/$c/g" $(pwd)/trytodecrypt_$id-decrypted.split
   fi
   index=$(($index+1))
done
