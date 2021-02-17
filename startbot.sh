#!/usr/bin/env bash
source_env() {
  [ "$#" -eq 1 ] && env="$1" || env=".env"
  [ -f "$env" ] || { echo "Env file $env doesn't exist"; return 1; }
  eval $(grep -Ev '^#|^$' "$env" | sed -e 's/=\(.*\)/="\1/g' -e 's/$/"/g' -e 's/^/export /')
}
source_env

#change this later to not do the example test but the tests for our actual bot
python3 ./tests/exampleTest/example_target.py $TECH_LAB_TOKEN