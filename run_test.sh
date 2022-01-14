#!/bin/sh -u

. ./tmp_config.sh

echo ---
echo APIキーなしで/hello0
curl "${HelloWorldApi}0"
echo "\n----"

echo APIキーなしで/hello
curl "${HelloWorldApi}"
echo "\n----"

echo APIキーつきで/hello
curl "${HelloWorldApi}" -H "x-api-key: ${ApiKey}"
echo "\n----"
