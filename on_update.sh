#!/bin/bash
set -e
set -u

TMP=$(mktemp .touchXXXX)
function tidy {
    rm $TMP
}
trap tidy EXIT

touch -t 197001010000 $TMP

if [[ -x clear ]]
then
    CLS=clear
else
    CLS=cls
fi

watch="$1"
shift

while true
do
    if [[ "$watch" -nt "$TMP" ]]
    then
        touch $TMP
        $CLS
        echo "$(date +%T) >> $@"
        "$@" | head -$(( ${LINES-40} - 2 ))
        echo "$? << $@"
    fi
    sleep 2
done

