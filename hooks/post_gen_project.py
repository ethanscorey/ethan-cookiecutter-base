import subprocess


if __name__ == "__main__":
    subprocess.run("pyenv install -s", shell=True, check=True)
    subprocess.run("./activate.sh", shell=True, check=True)
    subprocess.run("pre-commit install", shell=True, check=True)
