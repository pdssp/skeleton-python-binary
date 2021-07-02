# {{cookiecutter.project_name}} - {{cookiecutter.project_short_description}}
# Copyright (C) {{cookiecutter.year}} - {{cookiecutter.institute}} ({{cookiecutter.full_name}} for {{cookiecutter.consortium_name}})
#
# This file is part of {{cookiecutter.project_name}}.
#
# {{cookiecutter.project_name}} is free software: you can redistribute it and/or modify
# it under the terms of the {% if cookiecutter.open_source_license == 'GNU General Public License v3' -%}GNU General Public License{% elif cookiecutter.open_source_license == 'GNU Lesser General Public License v3' -%}GNU Lesser General Public License v3 {% elif cookiecutter.open_source_license == 'GNU Affero General Public License v3' -%}GNU Affero General Public License v3{% endif %} as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# {{cookiecutter.project_name}} is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# {% if cookiecutter.open_source_license == 'GNU General Public License v3' -%}GNU General Public License{% elif cookiecutter.open_source_license == 'GNU Lesser General Public License v3' -%}GNU Lesser General Public License v3 {% elif cookiecutter.open_source_license == 'GNU Affero General Public License v3' -%}GNU Affero General Public License v3{% endif %} for more details.
#
# You should have received a copy of the {% if cookiecutter.open_source_license == 'GNU General Public License v3' -%}GNU General Public License{% elif cookiecutter.open_source_license == 'GNU Lesser General Public License v3' -%}GNU Lesser General Public License v3 {% elif cookiecutter.open_source_license == 'GNU Affero General Public License v3' -%}GNU Affero General Public License v3{% endif %}
# along with {{cookiecutter.project_name}}.  If not, see <https://www.gnu.org/licenses/>.
FROM ubuntu:latest

LABEL maintainer="{{ cookiecutter.full_name }} <{{ cookiecutter.email }}>"

ARG BUILD_DATE
ARG VERSION
ARG DEBIAN_FRONTEND=noninteractive

# Labels (based on http://label-schema.org/rc1/)
LABEL \
    org.label-schema.schema-version="1.0" \
    org.label-schema.build-date=$BUILD_DATE \
    org.label-schema.name="cdm" \
    org.label-schema.description="{{ cookiecutter.project_short_description }}" \
    org.label-schema.url="https://github.com/pole-surfaces-planetaires/{{ cookiecutter.project_slug }}" \
    org.label-schema.vcs-url="https://github.com/pole-surfaces-planetaires/{{ cookiecutter.project_slug }}" \
    org.label-schema.vcs-ref=$VCS_REF \
    org.label-schema.vendor="{{ cookiecutter.consortium_name }}" \
    org.label-schema.version=$VERSION

RUN apt-get update && \
    apt-get install -y \
    software-properties-common apt-transport-https wget git\
    make python3-pip && \
    update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1 && \
    pip install setuptools && \
    git clone "https://github.com/pole-surfaces-planetaires/{{ cookiecutter.project_slug }}.git" && \
    cd {{ cookiecutter.project_slug }} && \
    make

# Custom prompt
RUN echo 'export PS1="\[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\[\033[01;31m\]\u@platoscope-dev\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$"' >> /etc/bash.bashrc

CMD ["{{cookiecutter.project_slug}}"]