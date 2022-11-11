# Custom .bashrc file to facilitate activating the project environment
# First, source user's .bashrc:
if [ -f ~/.bashrc ]; then
    . ~/.bashrc
fi

source .env
poetry install
source "$(poetry env info --path)/bin/activate"
