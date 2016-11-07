#!/usr/bin/env python
import pytest
from click.testing import CliRunner

from enshrine import to_json, to_yaml, main


VARS_YAML = """---
var1: value1
var2: value2
"""

INI_TEMPLATE = """[section]
value1: {{ var1 }}
value2: {{ var2 }}

"""


def _write_files():
    with open('vars.yaml', 'w') as f:
        f.write(VARS_YAML)
    with open('template.ini.jinja', 'w') as f:
        f.write(INI_TEMPLATE)


@pytest.mark.parametrize('data, expected', [
    ({'key': 'value'}, '{"key": "value"}'),
    ([1, 'two', 3], '[1, "two", 3]'),
    (None, 'null')
])
def test_to_json(data, expected):
    assert to_json(data) == expected


@pytest.mark.parametrize('data, expected', [
    ({'key': 'value'}, '{key: value}\n'),
    ([1, 'two', 3], '[1, two, 3]\n')
])
def test_to_yaml(data, expected):
    assert to_yaml(data) == expected


def test_main():
    runner = CliRunner()
    with runner.isolated_filesystem():
        _write_files()
        result = runner.invoke(main, ['vars.yaml', 'template.ini.jinja'])
        assert result.exit_code == 0
        assert result.output == '[section]\nvalue1: value1\nvalue2: value2\n\n'
