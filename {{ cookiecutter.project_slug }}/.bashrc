# Custom .bashrc file to facilitate activating the project environment
# First, source user's .bashrc:
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi

if [ -f .env ]; then
    source .env
fi

poetry install
source "$(poetry env info --path)/bin/activate"
