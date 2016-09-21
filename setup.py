#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages

requirements = [
    # TODO: put package requirements here
]
readme="""Write Python 3 language in thai lang."""

setup(
    name='thaipy',
    version='0.0.1',
    description="Write Python 3 language in thai lang.",
    long_description=readme,# + '\n\n' + history,
    author="Wannaphong Phatthiyaphaibun",
    author_email='wannaphong@yahoo.com',
    url='https://github.com/wannaphongcom/thaipy',
    packages=find_packages(),
    package_data={'pythainlp.corpus':['thaipos.json','thaiword.txt']},
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    scripts=['thaipy'],
    entry_points = """
    [console_scripts]
    thaipy = thaipy:commandline
    """,
    keywords='thaipy',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: Thai',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Code Generators',
        'Programming Language :: Python :: 3',
    ],
    test_suite='tests',
)