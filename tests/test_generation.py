import os
import pytest
import tempfile
from cookiecutter.main import cookiecutter

@pytest.fixture
def generate_project():
    """Fixture for generating a Cookiecutter project in a tmp directory"""
    with tempfile.TemporaryDirectory() as tempdir:
        cookiecutter(
            '.',
            no_input=True,
            output_dir=tempdir,
            extra_context={"project_name": "TestProject", "full_name": "John Doe", "email": "John.Doe@foo.com", "open_source_license": "MIT", "python_version": "3.12"},
        )
        yield tempdir


def test_project_structure(generate_project):
    """Check that the files and directories have been created."""
    project_dir = os.path.join(generate_project, "testproject")
    
    # Check the following files exist
    expected_files = [
        "tox.ini",
        "README.rst",
        "pyproject.toml",
        "Makefile",
        "LICENSE",
        "Dockerfile",
        "CONTRIBUTING.rst",
        "CHANGELOG",
        "AUTHORS.rst",
        ".pre-commit-config.yaml",
        ".gitignore",
        ".flake8",
        ".dockerignore",
        "tests/acceptance/docker_test.py",
        "tests/unit/monitoring_test.py",  
        "scripts/generate-changelog.bash",
        "scripts/init_remote_repo.bash",
        "scripts/install-hooks.bash",
        "scripts/license.py",
        "scripts/post-commit.bash",
        "docs/make.bat",
        "docs/Makefile",
        "docker/build.sh",
        "docker/Dockerfile",                      
        "testproject/__init__.py",
        "testproject/__main__.py",
        "testproject/_version.py",
        "testproject/testproject.py",
        "testproject/monitoring.py"       
    ]
    
    for file_name in expected_files:
        assert os.path.exists(os.path.join(project_dir, file_name)), f"{file_name} was not created"


def test_readme_content(generate_project):
    """Check the contain of the README is correctly generated."""
    readme_path = os.path.join(generate_project, "testproject", "README.rst")
    
    with open(readme_path, 'r') as readme_file:
        content = readme_file.read()
    
    assert "TestProject" in content, "The project name is not in the README"
    assert "John Doe" in content, "The author name is not in the README"
    assert "cookiecutter." not in content, "Some cookiecutter variables are not replaced"

def test_pyproject_toml(generate_project):
    """Check the contain of the pyproject.toml is correctly generated."""
    readme_path = os.path.join(generate_project, "testproject", "pyproject.toml")
    
    with open(readme_path, 'r') as readme_file:
        content = readme_file.read()

    assert "cookiecutter." not in content, "Some cookiecutter variables are not replaced"
    
def test_makefile(generate_project):
    """Check the Makefile is correctly generated."""
    readme_path = os.path.join(generate_project, "testproject", "Makefile")
    
    with open(readme_path, 'r') as readme_file:
        content = readme_file.read()

    assert "cookiecutter." not in content, "Some cookiecutter variables are not replaced"
    
def test_license(generate_project):
    """Check the License is correctly generated."""
    readme_path = os.path.join(generate_project, "testproject", "LICENSE")
    
    with open(readme_path, 'r') as readme_file:
        content = readme_file.read()

    assert "cookiecutter." not in content, "Some cookiecutter variables are not replaced"    
    
def test_Dockerfile(generate_project):
    """Check the Dockerfile is correctly generated."""
    readme_path = os.path.join(generate_project, "testproject", "Dockerfile")
    
    with open(readme_path, 'r') as readme_file:
        content = readme_file.read()

    assert "cookiecutter." not in content, "Some cookiecutter variables are not replaced"       
    
def test_contributing(generate_project):
    """Check the CONTRIBUTING.rst is correctly generated."""
    readme_path = os.path.join(generate_project, "testproject", "CONTRIBUTING.rst")
    
    with open(readme_path, 'r') as readme_file:
        content = readme_file.read()

    assert "cookiecutter." not in content, "Some cookiecutter variables are not replaced"         
 
    
def test_acceptance_tests(generate_project):
    """Check the docker_test is correctly generated."""
    readme_path = os.path.join(generate_project, "testproject", "tests", "acceptance", "docker_test.py")
    
    with open(readme_path, 'r') as readme_file:
        content = readme_file.read()

    assert "cookiecutter." not in content, "Some cookiecutter variables are not replaced"       
    
def test_unit_tests(generate_project):
    """Check the monitoring_test is correctly generated."""
    readme_path = os.path.join(generate_project, "testproject", "tests", "unit", "monitoring_test.py")
    
    with open(readme_path, 'r') as readme_file:
        content = readme_file.read()

    assert "cookiecutter." not in content, "Some cookiecutter variables are not replaced"      
    
def test_docker(generate_project):
    """Check the docker files are correctly generated."""
    readme_path = os.path.join(generate_project, "testproject", "docker", "build.sh")
    
    with open(readme_path, 'r') as readme_file:
        content = readme_file.read()

    assert "cookiecutter." not in content, "Some cookiecutter variables are not replaced"     
    
    readme_path = os.path.join(generate_project, "testproject", "docker", "Dockerfile")
    
    with open(readme_path, 'r') as readme_file:
        content = readme_file.read()

    assert "cookiecutter." not in content, "Some cookiecutter variables are not replaced"      
    
def test_main(generate_project):
    """Check the __main__ is correctly generated."""
    readme_path = os.path.join(generate_project, "testproject", "testproject", "__main__.py")
    
    with open(readme_path, 'r') as readme_file:
        content = readme_file.read()

    assert "cookiecutter." not in content, "Some cookiecutter variables are not replaced"      
    
def test_init(generate_project):
    """Check the __init__ is correctly generated."""
    readme_path = os.path.join(generate_project, "testproject", "testproject", "__init__.py")
    
    with open(readme_path, 'r') as readme_file:
        content = readme_file.read()

    assert "cookiecutter." not in content, "Some cookiecutter variables are not replaced"      