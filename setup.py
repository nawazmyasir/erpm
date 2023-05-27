#!/usr/bin/env python

from setuptools import setup

requirements = []  # add Python dependencies here
# e.g., requirements = ["PyYAML"]

setup(
    name='erpm',
    version='0.1',
    author='Ansible, Inc.',
    author_email='info@ansible.com',
    description='',
    long_description='',
    license='Apache License 2.0',
    keywords='ansible',
    url='https://github.com/nawazmyasir/awx-custom-credential-plugin-example',
    packages=['erpm'],
    include_package_data=True,
    zip_safe=False,
    setup_requires=[],
    install_requires=requirements,
    entry_points = {
        'awx.credential_plugins': [
            'erpm_plugin = erpm:erpm_plugin',
        ]
    }
)
