#!/bin/sh

set -x

echo $#
for var in "$@"
do 
    echo  "Hello $var"
done
