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
# You should have received a copy of the {% if cookiecutter.open_source_license == 'GNU General Public License v3' -%}GNU General Public License{% elif cookiecutter.open_source_license == 'GNU Lesser General Public License v3' -%}GNU Lesser General Public License{% elif cookiecutter.open_source_license == 'GNU Affero General Public License v3' -%}GNU Affero General Public License{% endif %}
# along with {{cookiecutter.project_name}}.  If not, see <https://www.gnu.org/licenses/>.
"""Project metadata."""
import toml
import os

project_root = os.path.dirname(os.path.dirname(__file__))
pyproject_path = os.path.join(project_root, "pyproject.toml")


with open(pyproject_path, "r") as file:
    pyproject_content = toml.load(file)

project_tool = pyproject_content.get("tool", {})
project_metadata = project_tool.get("poetry", {})

__name_soft__ = project_metadata.get("name", "unknown")
__version__ = project_metadata.get("version", "0.0.0")
__title__ = project_metadata.get("name", "unknown")
__description__ = project_metadata.get("description", "")
__url__ = project_metadata.get("homepage", "")
__author__ = project_metadata.get("authors", [{}])[0]
__author_email__ = project_metadata.get("authors", [{}])[0]
__license__ = project_metadata.get("license", "")
__copyright__ = "2024, {{cookiecutter.full_name}}"

