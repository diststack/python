#!/bin/bash

set -x
# while getopts :u:p: option
# do
# case $option in
# u) user=${OPTARG};;
# p) pwd=${OPTARG};;
# esac
# done
# echo $user
# echo $pwd

while getopts u:p: option
do
case $option in
u) user=$OPTARG ;;
p) pwd=$OPTARG;;
esac
done