# Custom .zshrc file to facilitate activating the project environment
# First, source user's .zshrc:
if [ -f "$HOME/.zshrc" ]; then
    source "$HOME/.zshrc"
fi


if [ -f .env ]; then
    source .env
fi

poetry install
source "$(poetry env info --path)/bin/activate"
