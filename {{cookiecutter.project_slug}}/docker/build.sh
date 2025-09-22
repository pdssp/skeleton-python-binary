#!/bin/sh
# {{cookiecutter.project_name}} - {{cookiecutter.project_description}}
# Copyright (C) {{cookiecutter.year}} - {{cookiecutter.institute}} ({{cookiecutter.full_name}} for {{cookiecutter.consortium_name}})
# This file is part of {{cookiecutter.project_name}} <{{ cookiecutter.project_url }}>
# SPDX-License-Identifier: {% if cookiecutter.open_source_license == 'GNU General Public License v3' -%}GPL-3.0-or-later{% elif cookiecutter.open_source_license == 'GNU Lesser General Public License v3' -%}LGPL-3.0-or-later{% elif cookiecutter.open_source_license == 'GNU Affero General Public License v3' -%}AGPL-3.0{% endif %}
docker build -t {{cookiecutter.docker_image_name}} -f docker/Dockerfile --build-arg POETRY_LOCK="$( stat poetry.lock )" .
