#!/bin/bash

echo "enter age"
read age

if (( $age >= 18 ))
then
echo " eligable to vote"
else
echo "not eligable to vote"
fi