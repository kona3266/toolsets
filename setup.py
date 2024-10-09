#!/usr/bin/env python
import common_tools
from pathlib import Path
from setuptools import setup, find_packages

def read(*names):
    values = {}
    for name in names:
        value = ''
        for extension in ('.txt', '.md'):
            filename = name + extension
            if Path(filename).is_file():
                with open(filename) as f:
                    value = f.read()
                break
        values[name] = value
    return values


description = '''%(README)s
%(CHANGES)s''' % read('README', 'CHANGES')

setup(
        name = 'common_tools',
        version = common_tools.__version__,
        description = 'a set of tools',
        long_description = description,
        packages = find_packages(),
        entry_points={'console_scripts': [
            'tree-cli = common_tools.tree_cli:cmd_runner',
            'heapsort = common_tools.heapsort:runner',
            'vxlan-pcap = common_tools.pcap_vxlan:runner',
        ]},
        install_requires=[
            'python-libpcap',
            'Cython'
        ]
)
