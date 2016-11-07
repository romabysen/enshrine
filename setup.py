from setuptools import setup

setup(
    name='enshrine',
    version='0.1.0',
    license='New BSD',
    py_modules=['enshrine'],
    install_requires=[
        'Jinja2>=2.8',
        'Click>=6.6',
        'PyYaml>=3.12'
    ],
    entry_points='''
        [console_scripts]
        enshrine=enshrine:main
    ''',
)
