#!/usr/bin/env bash
source_env() {
  [ "$#" -eq 1 ] && env="$1" || env=".env"
  [ -f "$env" ] || { echo "Env file $env doesn't exist"; return 1; }
  eval $(grep -Ev '^#|^$' "$env" | sed -e 's/=\(.*\)/="\1/g' -e 's/$/"/g' -e 's/^/export /')
}
source_env

python3 ./exampleTest/example_tester.py $TECH_LAB_BOT_ID ODExMzc1MzUwNzk3Njk3MDU0.YCxSLg.oMhShjAIqxUH9V3IB7qfrCEDvSs -c $CHANNEL_ID -r all