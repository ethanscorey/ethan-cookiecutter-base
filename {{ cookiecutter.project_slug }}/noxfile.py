from nox_poetry import session

LOCATIONS = ("src", "tests", "noxfile.py")
VERSIONS = ["{{ cookiecutter.python_version }}"]


@session(python=VERSIONS)
def tests(session: session) -> None:
    """Run test suit, skipping e2e tests by default.

    Arguments
    ---------
    session : session
        The nox session.
    """
    args = session.posargs or ["--cov", "-m", "not e2e"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)


@session(python=VERSIONS)
def format_files(session: session) -> None:
    """Format Python files with ruff.

    Arguments
    ---------
    session : session
        The nox session.
    """
    args = session.posargs or LOCATIONS
    session.install("ruff")
    session.run("ruff", "format", *args)


@session(python=VERSIONS)
def safety(session):
    """Check pyproject.toml for known vulnerabilities.

    Arguments
    ---------
    session : session
        The nox session.

    """
    session.install("safety")
    session.run("safety", "check", "--file=pyproject.toml", "--full-report")


@session(python=VERSIONS)
def lint(session: session) -> None:
    """Lint Python files with ruff.

    Arguments
    ---------
    session : session
        The nox session.
    """
    args = session.posargs or LOCATIONS
    session.install("ruff")
    session.run("ruff", "check", "--fix", *args)


@session(name="doc-lint", python=VERSIONS[0])
def doc_lint(session: session) -> None:
    """Lint docstrings with pydoclint.

    Arguments
    ---------
    session : session
        The nox session.
    """
    args = session.posargs or LOCATIONS
    session.install("pydoclint")
    session.run("pydoclint", *args)


{% if cookiecutter.mypy == "y" %}
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
