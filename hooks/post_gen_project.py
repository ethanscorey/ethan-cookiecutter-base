import subprocess


if __name__ == "__main__":
    subprocess.run("conda env create -f environment.yml", shell=True, check=True)
    subprocess.run("./activate.sh", shell=True, check=True)
