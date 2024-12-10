# -*- coding: utf-8 -*-
# {{cookiecutter.project_name}} - {{cookiecutter.project_description}}
# Copyright (C) {{cookiecutter.year}} - {{cookiecutter.institute}} ({{cookiecutter.full_name}} for {{cookiecutter.consortium_name}})
# This file is part of {{cookiecutter.project_name}} <{{ cookiecutter.project_url }}>
# SPDX-License-Identifier: {% if cookiecutter.open_source_license == 'GNU General Public License v3' -%}GPL-3.0-or-later{% elif cookiecutter.open_source_license == 'GNU Lesser General Public License v3' -%}LGPL-3.0-or-later{% elif cookiecutter.open_source_license == 'GNU Affero General Public License v3' -%}AGPL-3.0{% endif %}

ARG DEBIAN_NAME="bullseye"
ARG PYTHON_VERSION="{{cookiecutter.python_version}}"
FROM python:${PYTHON_VERSION}-slim-${DEBIAN_NAME} AS base

WORKDIR /app
RUN apt-get update -qq \
      && apt upgrade --yes \
      && apt-get clean all \
      && rm -rf /var/lib/apt/lists/*

FROM base AS builder
ARG CI_JOB_TOKEN
ENV project_url={{ cookiecutter.project_url }}.git

WORKDIR /app

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
         git  \
      && apt-get clean all \
      && rm -r /var/lib/apt/lists/*

RUN pip install poetry && poetry config installer.max-workers 10 && poetry config virtualenvs.create false
COPY . .
RUN make release && VERSION=$(poetry version -s) && pip install dist/{{ cookiecutter.project_slug }}-${VERSION}.tar.gz

FROM python:{{cookiecutter.python_version}}-slim-bullseye AS release
ARG BUILD_DATE
ARG VERSION
ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /app

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

# Get the installed libraries and application from the ealier stage
COPY --from=builder /usr/local/ /usr/local/

# Regenerate the shared-library cache
RUN ldconfig

ENTRYPOINT ["{{ cookiecutter.project_slug }}"]
