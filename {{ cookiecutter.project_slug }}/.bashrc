# Custom .bashrc file to facilitate activating the project environment
# First, source user's .bashrc:
if [ -f ~/.bashrc ]; then
    . ~/.bashrc
fi

# Then, activate project conda env and install poetry dependencies:
# Note that this only works if the user has run `conda init` in their own
# Bash environment.
conda activate {{ cookiecutter.project_slug }}
poetry install
