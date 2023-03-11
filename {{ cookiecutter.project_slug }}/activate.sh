#!/bin/sh

# Determine the user's current shell
SHELL_NAME=$(basename "$SHELL")


if [ "$SHELL_NAME" = "bash" ]; then
  exec bash --rcfile .bashrc -i
elif [ "$SHELL_NAME" = "zsh" ]; then
  exec zsh -i -c 'source .zshrc && exec zsh'
else
  echo "Unsupported shell: $SHELL_NAME"
  exit 1
fi
