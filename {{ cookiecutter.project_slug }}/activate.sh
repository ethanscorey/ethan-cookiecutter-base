#!/bin/sh

# Determine the user's current shell
SHELL_NAME=$(basename "$SHELL")

# Set the appropriate activation command based on the shell
if [ $SHELL_NAME = "bash" ]; then
  ACTIVATE_CMD="bash"
elif [ $SHELL_NAME = "zsh" ]; then
  ACTIVATE_CMD="zsh"
else
  echo "Unsupported shell: $SHELL_NAME"
  exit 1
fi

if [ "$SHELL_NAME" = "bash" ]; then
  exec "$ACTIVATE_CMD" --rcfile .bashrc
elif [ "$SHELL_NAME" = "zsh" ]; then
  exec "$ACTIVATE_CMD" --rcs .zshrc
fi
