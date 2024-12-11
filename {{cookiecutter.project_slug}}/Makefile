.DEFAULT_GOAL := init
.PHONY: upload-test-pypi upload-prod-pypi docker add_req_prod add_req_dev add_major_version add_minor_version add_patch_version add_premajor_version add_preminor_version add_prepatch_version add_prerelease_version prepare-dev install-dev data help lint tests coverage upload-prod-pypi upload-test-pypi update_req update_req_dev pyclean doc doc-pdf visu-doc-pdf visu-doc tox licences check_update update_latest_dev update_latest_main show_deps_main show_deps_dev show_obsolete
VENV = ".venv"
VENV_RUN = ".{{cookiecutter.project_slug}}"

define PROJECT_HELP_MSG

Usage:\n
	\n
    make help\t\t\t             show this message\n
	\n
	-------------------------------------------------------------------------\n
	\t\tInstallation\n
	-------------------------------------------------------------------------\n
	make\t\t\t\t                Install {{ cookiecutter.project_slug }} in the system (root)\n
	make user\t\t\t 			Install {{ cookiecutter.project_slug }} for non-root usage\n
	\n
	-------------------------------------------------------------------------\n
	\t\tDevelopment\n
	-------------------------------------------------------------------------\n
	make prepare-dev\t\t 		Prepare Development environment\n
	make install-dev\t\t 		Install COTS and {{ cookiecutter.project_slug }} for development purpose\n
	make tests\t\t\t             Run units and integration tests\n
	\n
	make doc\t\t\t 				Generate the documentation\n
	make doc-pdf\t\t\t 			Generate the documentation as PDF\n
	make visu-doc-pdf\t\t 		View the generated PDF\n
	make visu-doc\t\t\t			View the generated documentation\n
	\n
	make release\t\t\t 			Release the package as tar.gz\n
	make upload-test-pypi\t\t   Upload the pypi package on the test platform\n
	make upload-prod-pypi\t\t   Upload the pypi package on the prod platform\n	
	\n
	make pyclean\t\t\t		Clean .pyc files and __pycache__ directories\n
	\n
	make add_req_prod pkg=<name>\t Add the package in the dependencies of .toml\n
	make add_req_dev pkg=<name>\t Add the package in the DEV dependencies of .toml\n
	\n
	make docker\t\t\t Create the docker image\n	
	\n
	-------------------------------------------------------------------------\n
	\t\tVersion\n
	-------------------------------------------------------------------------\n	
	make version\t\t\t		Display the version\n
	make add_major_version\t\t	Add a major version\n
	make add_minor_version\t\t	Add a major version\n
	make add_patch_version\t\t	Add a major version\n
	make add_premajor_version\t	Add a pre-major version\n
	make add_preminor_version\t	Add a pre-minor version\n
	make add_prepatch_version\t	Add a pre-patch version\n
	make add_prerelease_version\t	Add a pre-release version\n
	\n
	-------------------------------------------------------------------------\n
	\t\tMaintenance (use make install-dev before using these tasks)\n
	-------------------------------------------------------------------------\n	
	make check_update\t\t 		Check the COTS update\n
	make update_req\t\t			Update the version of the packages in the authorized range in toml file\n
	make update_latest_dev\t\t	Update to the latest version for development\n
	make update_latest_main\t 	Update to the latest version for production\n
	make show_deps_main\t\t 	Show main COTS for production\n 
	make show_deps_dev\t\t 		Show main COTS for development\n 
	make show_obsolete\t\t		Show obsolete COTS\n
	\n
	-------------------------------------------------------------------------\n
	\t\tOthers\n
	-------------------------------------------------------------------------\n
	make licences\t\t\t		Display the list of licences\n
	make coverage\t\t\t 	Coverage\n
	make lint\t\t\t			Lint\n
	make tox\t\t\t 			Run all tests\n

endef
export PROJECT_HELP_MSG


#Show help
#---------
help:
	echo $$PROJECT_HELP_MSG


#
# Sotware Installation in the system (need root access)
# -----------------------------------------------------
#
init:
	poetry install --only=main

#
# Sotware Installation for user
# -----------------------------
# This scheme is designed to be the most convenient solution for users
# that don’t have write permission to the global site-packages directory or
# don’t want to install into it.
#
user:
	poetry install --only=main

{%- if cookiecutter.use_pyenv -%}
#Comment line is required to properly write pyenv-dev
prepare-dev:
	@if command -v pyenv >/dev/null; then \
		echo "pyenv is installed, proceeding with setup..."; \
	else \
		echo "pyenv is not installed. Please install pyenv first."; \
		exit 1; \
	fi
	git config --global init.defaultBranch main
	git init
	echo "echo \"Using Virtual env for {{cookiecutter.project_slug}}.\"" > ${VENV_RUN}
	echo "echo \"Please, type 'deactivate' to exit this virtual env.\"" >> ${VENV_RUN} 
	PYTHON_VERSION={{cookiecutter.python_version}} && \
	pyenv install -s $$PYTHON_VERSION && \
	FULL_PYTHON_VERSION=$$(pyenv versions --bare --skip-aliases | grep $$PYTHON_VERSION | sort -V | tail -1) && \
	PYENV_ROOT=$$(pyenv root) && \
	PYENV_PYTHON="$$PYENV_ROOT/versions/$$FULL_PYTHON_VERSION/bin/python" && \
	echo "$$PYENV_PYTHON -m venv --prompt {{cookiecutter.project_slug}} ${VENV}" >> ${VENV_RUN} && \
	echo "export PYTHONPATH=." >> ${VENV_RUN} && \
	echo "export PATH=`pwd`/${VENV}/bin:$$PATH" >> ${VENV_RUN} && \
	echo "source '`pwd`/${VENV}/bin/activate'" >> ${VENV_RUN} && \
	scripts/install-hooks.bash && \
	echo "\nnow source this file: \033[31msource ${VENV_RUN}\033[0m"
{%- else -%}
#Comment line is required to properly write pyenv-dev
prepare-dev:
	git config --global init.defaultBranch main 
	git init
	echo "echo \"Using Virtual env for {{cookiecutter.project_slug}}.\"" > ${VENV_RUN}
	echo "echo \"Please, type 'deactivate' to exit this virtual env.\"" >> ${VENV_RUN} 
	echo "python3 -m venv --prompt {{cookiecutter.project_slug}} ${VENV} && \
	export PYTHONPATH=. && \
	export PATH=`pwd`/${VENV}/bin:${PATH}" >> ${VENV_RUN} && \
	echo "source \"`pwd`/${VENV}/bin/activate\"" >> ${VENV_RUN} && \
	scripts/install-hooks.bash && \
	echo "\nnow source this file: \033[31msource ${VENV_RUN}\033[0m"
{% endif %}

install-dev:
	poetry install && poetry run pre-commit install && poetry run pre-commit autoupdate

coverage:  ## Run tests with coverage
	poetry run coverage erase
	poetry run coverage run --include={{cookiecutter.project_slug}}/* -m pytest --ignore=./tests/msap_data -ra
	poetry run coverage report -m

lint:  ## Lint and static-check
	poetry run flake8 --ignore=E203,E266,E501,W503,F403,F401 --max-line-length=79 --max-complexity=18 --select=B,C,E,F,W,T4,B9 {{cookiecutter.project_slug}}
	poetry run pylint {{cookiecutter.project_slug}}
	poetry run mypy --install-types --non-interactive {{cookiecutter.project_slug}}

tests:  ## Run tests
	poetry run pytest --ignore=./tests/msap_data

tox:
	poetry run tox -e py310

doc:
	make licences
	rm -rf docs/source/_static/coverage
	poetry run pytest --ignore=./tests/msap_data -ra --html=docs/source/_static/report.html
	poetry run make coverage
	poetry run coverage html -d docs/source/_static/coverage
	poetry run make html -C docs

doc-pdf:
	make doc && poetry run make latexpdf -C docs

visu-doc-pdf:
	acroread docs/build/latex/{{cookiecutter.project_slug}}.pdf

visu-doc:
	firefox docs/build/html/index.html

release:
	poetry build

version:
	poetry version -s

add_major_version:
	poetry version major 
	poetry run git tag `poetry version -s`

add_minor_version:
	poetry version minor
	poetry run git tag `poetry version -s`

add_patch_version:
	poetry version patch
	poetry run git tag `poetry version -s`

add_premajor_version:
	poetry version premajor

add_preminor_version:
	poetry version preminor

add_prepatch_version:
	poetry version prepatch 

add_prerelease_version:
	poetry version prerelease

add_req_prod:
	poetry add "$(pkg)"

add_req_dev:
	poetry add -G dev "$(pkg)"

upload-test-pypi:
	flit publish --repository pypitest

upload-prod-pypi:
	flit publish	

licences:
	poetry run python3 scripts/license.py

check_update:
	poetry show -l
	
update_req:
	poetry update

update_latest_dev:
	packages=$$(poetry show -T --only=dev | grep -oP "^\S+"); \
	packages_latest=$$(echo $$packages | tr '\n' ' ' | sed 's/ /@latest /g'); \
	poetry add -G dev $$packages_latest
	
update_latest_main:
	packages=$$(poetry show -T --only=main | grep -oP "^\S+"); \
	packages_latest=$$(echo $$packages | tr '\n' ' ' | sed 's/ /@latest /g'); \
	poetry add -G main $$packages_latest

show_deps_main:
	poetry show -T --only=main

show_deps_dev:
	poetry show -T --only=dev

show_obsolete:
	poetry show -o

pyclean:
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

docker:
	sh docker/build.sh
