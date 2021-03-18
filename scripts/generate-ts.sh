#!/bin/bash
echo "==> Generating Tree Shakable Assets..."
rm -rf prepublish/
npx svg-to-ts --conversionType constants -s ./icons -o ./prepublish
sleep 1
echo "==> Assets Generated"
