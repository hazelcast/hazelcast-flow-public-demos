#! /bin/sh

if [ "x$1" = "x" ]; then
  echo "missing script name"
  echo "usage: $0 <shell|SCRIPT>"
  exit 1
fi

if [ "$1" =  "shell" ]; then
  exec /bin/bash
fi

export PATH=$HOME/.local/bin:$PATH

exec "$@"
