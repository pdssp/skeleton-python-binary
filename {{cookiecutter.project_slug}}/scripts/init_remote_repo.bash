#!/usr/bin/env bash
git branch -M main
git remote add origin {{ cookiecutter.project_url }}.git
git push -u origin main
