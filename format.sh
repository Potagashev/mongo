#!/bin/sh -e
set -x

i=0
max_tries=3

while [ $i -lt $max_tries ] ;
do
	if pre-commit run --all-files ; then
		i=$(( max_tries ))
	else
		i=$(( i+1 ))
	fi
	mypy --show-error-codes --disable-error-code=import --disable-error-code=misc ./src && true
done
