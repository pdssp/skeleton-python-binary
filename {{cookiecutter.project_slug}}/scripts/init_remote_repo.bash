#!/usr/bin/env bash
git branch -M main
git remote add origin https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
git push -u origin main
