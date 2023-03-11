"""Just test that we can import the package."""
import {{ cookiecutter.project_slug }}


def test_installed() -> None:
    """Test that project can be imported."""
    assert {{ cookiecutter.project_slug }}
