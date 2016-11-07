#!/usr/bin/env python
import json
import os
import os.path

from jinja2 import Environment, FileSystemLoader, StrictUndefined
import click
import yaml


def combine_vars(variable_files):
    data = {}
    for f in variable_files:
        v = yaml.load(f)
        data.update(v)
    return data


def to_json(data):
    return json.dumps(data)


def to_yaml(data):
    return yaml.dump(data)


def render_template(template_dir, template, variables, output):
    env = Environment(loader=FileSystemLoader(template_dir), keep_trailing_newline=True,
                      undefined=StrictUndefined)
    env.filters['to_json'] = to_json
    env.filters['to_yaml'] = to_yaml
    tpl = env.get_template(template)
    if 'env' in variables:
        del variables['env']
    output.write(tpl.render(**variables, env=os.environ))


@click.command()
@click.option('-o', 'output_file', default='-', type=click.File('w'), help='Output file. Default "stdout"')
@click.argument('variable_files', nargs=-1, required=True, type=click.File('r'))
@click.argument('template_file', nargs=1, type=click.Path(exists=True, dir_okay=False))
def main(variable_files, template_file, output_file):
    """A simple file template system. """
    tpl_vars = combine_vars(variable_files)
    file_name = os.path.basename(template_file)
    dir_name = os.path.dirname(template_file)
    render_template(dir_name, file_name, tpl_vars, output_file)

if __name__ == '__main__':
    main()
