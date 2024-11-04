import platform
import sys
import os

def is_compatible_with_plateform(minimal_python_version_wanted):
    major_version_wanted, minor_version_wanted = minimal_python_version_wanted.split(".")
    python_version = platform.python_version_tuple()
    major_version, minor_version, _ = python_version 
    return major_version_wanted == major_version and  int(minor_version_wanted) <= int(minor_version)

def is_compatible_with_gitlab_docker(minimal_python_version_wanted):
    major_version_wanted, minor_version_wanted = minimal_python_version_wanted.split(".")
    python_version = "3.13."
    major_version, minor_version, _ = python_version.split(".") 
    return major_version_wanted == major_version and  int(minor_version_wanted) <= int(minor_version)

def is_pyenv_installed():
    path_directories = os.environ.get('PATH', '').split(os.pathsep)

    # Look at the install directory of pyenv in PATH
    for directory in path_directories:
        if 'pyenv' in directory:
            return True

    return False

def is_pyenv_selected(pyenv):
    return pyenv.lower() in ("yes", "true", "t", "1")


minimal_python_version_wanted = "{{ cookiecutter.python_version }}"
pyenv_wanted = "{{ cookiecutter.use_pyenv }}"


if is_compatible_with_plateform(minimal_python_version_wanted) and is_compatible_with_gitlab_docker(minimal_python_version_wanted):
    if is_pyenv_selected(pyenv_wanted):
        if is_pyenv_installed():
            sys.exit(0)
        else:
            print ("Please set use_pyenv=False or install it")
            sys.exit(1)     
    else:
         sys.exit(0)      
elif is_pyenv_selected(pyenv_wanted):
    if is_pyenv_installed():
        sys.exit(0)
    else:
        print ("Please install pyenv")
        sys.exit(1)      
else:
    print("Please set use_pyenv=True with this python version")
    sys.exit(1)
    

