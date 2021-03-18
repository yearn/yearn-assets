#!/bin/sh
me=`basename "$0"`

if [ "$me" = ".common.sh" ];then
  echo >&2 "This script is not expected to be run separately."
  exit 1
fi

bold=$(tput bold)
normal=$(tput sgr0)

mkdir -p dist/tokens/png
mkdir -p svg-dist/tokens
mkdir -p dist/assets
