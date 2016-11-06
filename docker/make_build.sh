#!/bin/bash
# ------------------------------------------------------------------
# [Masaya Ogushi] Build DyNet shell
#
#    library for Unix shell scripts.
#    Usage
#           you have to use this script `sudo` command in the docker enviroment
#    Reference
#        http://dev.classmethod.jp/tool/jq-manual-japanese-translation-roughly/
#
# ------------------------------------------------------------------
if [ $# -ne 1 ]; then
    echo "$0 [dynet or lamtram-base or lamtram]"
    exit 1
fi

# -- Body ---------------------------------------------------------
#  SCRIPT LOGIC GOES HERE
cp -r ../dynet dynet
if [ $1 == "dynet" ]
then
    make test-dynet
elif [ $1 == "lamtram-base" ]
then
    make test-lamtram-base
elif [ $1 == "lamtram" ]
then
    make test-lamtram
fi
# -----------------------------------------------------------------