#!/bin/bash
mkdir my_test_folder
cd my_test_folder
pwd
for i in {1..5}
do
   touch "file_$i.txt"
   echo "Created file_$i.txt"
done