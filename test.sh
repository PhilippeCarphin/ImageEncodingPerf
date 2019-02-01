#!/bin/bash

# python src/encoder.py --algo pairs --input res/cats_are_evil.jpeg
# exit 0
# python src/encoder.py --algo pairs --input res/lipsum.txt
echo "["
for file in $(ls res) ; do
    python src/encoder.py --algo pairs --input res/$file
done

echo "]"

