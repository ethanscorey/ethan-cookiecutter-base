from nox_poetry import session

LOCATIONS = ("src", "tests", "noxfile.py")
VERSIONS = ["{{ cookiecutter.python_version }}"]


@session(python=VERSIONS)
def tests(session):
    args = session.posargs or ["--cov", "-m", "not e2e"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)


@session(python=VERSIONS)
def lint(session):
    args = session.posargs or LOCATIONS
    session.install(
        "flake8",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-isort",
    )
    session.run("flake8", *args)


@session(python=VERSIONS)
def safety(session):
    session.install("safety")
    session.run("safety", "check", "--file=pyproject.toml", "--full-report")


{% if cookiecutter.mypy == "y" -%}
@session(python=VERSIONS)
def mypy(session):
    args = session.posargs or ["src"]
    session.install(".")
    session.install("mypy")
    session.run("mypy", "--install-types")
    session.run("mypy", *args)


{% endif %}
@session(python=VERSIONS)
def format(session):
    args = session.posargs or LOCATIONS
    session.install("black", "isort")
    session.run("black", *args)
    session.run("isort", *args)
