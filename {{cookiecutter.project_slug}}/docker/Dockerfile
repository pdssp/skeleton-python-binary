# -*- coding: utf-8 -*-
# {{cookiecutter.project_name}} - {{cookiecutter.project_description}}
# Copyright (C) {{cookiecutter.year}} - {{cookiecutter.institute}} ({{cookiecutter.full_name}} for {{cookiecutter.consortium_name}})
# This file is part of {{cookiecutter.project_name}} <{{ cookiecutter.project_url }}>
# SPDX-License-Identifier: {% if cookiecutter.open_source_license == 'GNU General Public License v3' -%}GPL-3.0-or-later{% elif cookiecutter.open_source_license == 'GNU Lesser General Public License v3' -%}LGPL-3.0-or-later{% elif cookiecutter.open_source_license == 'GNU Affero General Public License v3' -%}AGPL-3.0{% endif %}

# Stage 1: Builder
FROM python:{{cookiecutter.python_version}}-slim-bullseye AS builder

# Set environment variables to optimize Python execution in Docker:
# - PYTHONDONTWRITEBYTECODE: Prevents Python from writing bytecode (.pyc) files to disk, reducing image size and avoiding potential conflicts.
# - PYTHONUNBUFFERED: Ensures Python outputs are sent directly to terminal without buffering, providing real-time logging and error visibility.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apt-get update -qq \
      && apt upgrade --yes \
      && apt-get -y --no-install-recommends install \
         build-essential \
         ca-certificates \
         gdb \
         gfortran \
         wget \
         file \
         apt-utils \
         curl \
         git  \
      && apt-get clean all \
      && rm -r /var/lib/apt/lists/*


# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python -

# Copy only dependencies
WORKDIR /app
COPY pyproject.toml poetry.lock /app/

# Install dependencies
RUN poetry install --no-dev --no-root

# Stage 2: Runtime
FROM python:{{cookiecutter.python_version}}-slim-bullseye AS runtime

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Labels (based on OCI Image Format Specification)
LABEL \
    org.opencontainers.image.version=$VERSION \
    org.opencontainers.image.created=$BUILD_DATE \
    org.opencontainers.image.title="{{ cookiecutter.project_name }}" \
    org.opencontainers.image.ref.name="{{ cookiecutter.project_slug }}" \
    org.opencontainers.image.description="{{ cookiecutter.project_description }}" \
    org.opencontainers.image.licenses="{{ cookiecutter.open_source_license }}" \
    org.opencontainers.image.source="{{ cookiecutter.project_url }}" \
    org.opencontainers.image.documentation="{{ cookiecutter.project_web_site }}" \
    org.opencontainers.image.vendor="{{ cookiecutter.consortium_name }}" \
    org.opencontainers.image.authors="{{ cookiecutter.full_name }} <{{ cookiecutter.email }}>"

# Copy dependencies from builder stage
COPY --from=builder /usr/local/lib/python{{cookiecutter.python_version}}/site-packages /usr/local/lib/python{{cookiecutter.python_version}}/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /{{project_slug}} /{{project_slug}}

# Set working directory
WORKDIR /app

# Copy application code
COPY . /app

CMD [{{project_slug}}]
