#!/bin/bash

id=$1

main_folder=$(pwd)/trytodecrypt_$id

# check if editing file exists and move to decryptable format
if [ ! -f $(pwd)/trytodecrypt_$id.split ]; then
   echo $2 | sed 's/\(......\)/\1 \n/g' | sed 's/\(..\)/\1 /g' > $(pwd)/trytodecrypt_$id.split
fi

if [ ! -d $main_folder ]; then
   mkdir $main_folder
fi

# calculate the unique difference when using single character encrypt with the algorithm
index=0
for c in {{0..9},{a..z},{A..Z},-,_,.}; do
   if [ ! -f $main_folder/$index.char ]; then
      str=$(printf -- "$c%.0s" {1..3})
      curl -s "http://api.trytodecrypt.com/encrypt?key=95dc64bedb5451dde3ab8bb9b36a3431&id=15&text=$str" | sed 's/\(......\)/\1\n/g' | sed 's/\(..\)/\1 /g' > $main_folder/$index.char
      hxn=$(cat $main_folder/$index.char | tail -n1 | awk '{print $1}')
      hxo=$(cat $main_folder/$index.char | head -n1 | awk '{print $1}')
      echo $((0x$hxn - 0x$hxo)) > $main_folder/$index.hid
   fi
   index=$(($index+1))
done

# calculate decimal value of the difference then output to the edited file
num_row=$(cat $(pwd)/trytodecrypt_$id.split | wc -l)
for i in $(seq 2 $num_row); do
   for j in {1..3}; do
      hxn=$(cat $(pwd)/trytodecrypt_$id.split | head -n$i | tail -n1 | awk -v j=$j 'BEGIN{OFS=IFS="\t"} {print $j}')
      hxo=$(cat $(pwd)/trytodecrypt_$id.split | head -n1 | awk -v j=$j 'BEGIN{OFS=IFS="\t"} {print $j}')
      printf -v hxn=$hxn -v hxo=$hxo "$((0x$hxn - 0x$hxo))\t" >> $(pwd)/trytodecrypt_$id-edited.split
   done
   printf "\n" >> $(pwd)/trytodecrypt_$id-edited.split
done

cp $(pwd)/trytodecrypt_$id-edited.split $(pwd)/trytodecrypt_$id-decrypted.split

# replace the decimal value of the difference with alphabetical characters
index=0
for c in {{0..9},{a..z},{A..Z},-,_,.}; do
   hid=$(cat $main_folder/$index.hid)
   if $(grep -Fwq $hid $(pwd)/trytodecrypt_$id-decrypted.split); then
      sed -i "s/$hid/$c/g" $(pwd)/trytodecrypt_$id-decrypted.split
   fi
   index=$(($index+1))
done
