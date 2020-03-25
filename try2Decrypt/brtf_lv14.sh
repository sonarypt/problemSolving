#!/bin/bash

id=$1

# check if editing file exists and move to decryptable format
if [ ! -f $(pwd)/trytodecrypt_$id.split ]; then
   echo $2 | sed 's/\(......\)/\1 \n/g' | sed 's/\(..\)/\1 /g' > $(pwd)/trytodecrypt_$id.split
fi

# calculate decimal value of the difference then output to the edited file
num_row=$(cat $(pwd)/trytodecrypt_$id.split | wc -l)
for i in $(seq 2 $num_row); do
   for j in {1..3}; do
      hxn=$(cat $(pwd)/trytodecrypt_$id.split | head -n$i | tail -n1 | awk -v j=$j 'BEGIN{OFS=IFS="\t"} {print $j}')
      hxo=$(cat $(pwd)/trytodecrypt_$id.split | head -n1 | awk -v j=$j 'BEGIN{OFS=IFS="\t"} {print $j}')
      printf "$((0x$hxn - 0x$hxo))\t" >> $(pwd)/trytodecrypt_$id-edited.split
   done
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
