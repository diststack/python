#! /bin/sh

set -x
start=$1
end=$2

while [ $start -le $end ]
#while (( $start <= $end ))
do
    echo $start
    start=$((start+1))
done

echo "shift usage:"
while (( $# ))
 do
    echo $1
    shift
 done