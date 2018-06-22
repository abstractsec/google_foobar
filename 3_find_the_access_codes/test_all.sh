#!/usr/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

for f in "${DIR}/"*."py"; do
    echo "# " $f
    python2 $f
done