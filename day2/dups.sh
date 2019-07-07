#!/bin/bash
input="./input"
while IFS= read -r line
do
  echo Beginning of line
  echo $line
  echo $line | sed -n '1{p;q}' | grep -o . | sort | tr '\n' ' ' 
  echo
done < "$input"
