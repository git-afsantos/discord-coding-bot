# SPDX-License-Identifier: MIT
# Copyright © 2023 André Santos

###############################################################################
# Imports
###############################################################################

from pathlib import Path
from setuptools import find_packages, setup

###############################################################################
# Constants
###############################################################################

PROJECT = 'discord-coding-bot'
PYTHON_PKG = 'discodebot'
HERE = Path(__file__).parent

###############################################################################
# Utility
###############################################################################


def read(filename):
    # Utility function to read the README, etc..
    # Used for the long_description and other fields.
    return (HERE / filename).read_text(encoding='utf-8')


###############################################################################
# Setup
###############################################################################


setup(
    name=PROJECT,
    use_scm_version={
        'version_scheme': 'no-guess-dev',
        'local_scheme': 'dirty-tag',
        'fallback_version': '0.1.0',
    },
    description='Discord Coding Bot',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url=f'https://github.com/git-afsantos/{PROJECT}',
    author='André Santos',
    author_email='contact.andre.santos@gmail.com',
    license='MIT',
    keywords='discord, programming, bot',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    package_data={},  # {PYTHON_PKG: ['dir/*.file']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
    ],
    entry_points={
        'console_scripts': [f'{PROJECT}={PYTHON_PKG}.cli:main'],
    },
    python_requires='>=3.8, <4',
    install_requires=[
        'attrs>=22.1',
        'discord.py>=2.2',
        'python-dotenv>=1.0',
        'pyautogui',
        # 'pyyaml>=5.3.1',
    ],
    extras_require={
        'dev': ['pytest', 'tox'],
    },
    zip_safe=False,
    project_urls={
        'Source': f'https://github.com/git-afsantos/{PROJECT}/',
        'Tracker': f'https://github.com/git-afsantos/{PROJECT}/issues',
        # 'Say Thanks!': 'http://saythanks.io/to/oatspear',
    },
)
