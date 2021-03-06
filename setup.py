#!/usr/bin/env python
from os.path import dirname, join

from emailauth import VERSION


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version(version):
    """
    Returns a PEP 386-compliant version number from ``version``.
    """
    assert len(version) == 5
    assert version[3] in ('alpha', 'beta', 'rc', 'final')
    
    # Now build the two parts of the version number:
    # main = X.Y[.Z]
    # sub = .devN - for pre-alpha releases
    #     | {a|b|c}N - for alpha, beta and rc releases
    
    parts = 2 if version[2] == 0 else 3
    main = '.'.join(str(x) for x in version[:parts])
    
    sub = ''
    if version[3] != 'final':
        mapping = {'alpha': 'a', 'beta': 'b', 'rc': 'c'}
        sub = mapping[version[3]] + str(version[4])
    
    return main + sub


with open(join(dirname(__file__), 'README.rst')) as f:
    long_description = f.read()


setup(
    name='emailauth',
    version=get_version(VERSION),
    
    description='Seamless email authentication for Django',
    long_description=long_description,
    url='http://github.com/dfunckt/django-emailauth',
    author='Akis Kesoglou',
    author_email='akiskesoglou@gmail.com',
    maintainer='Akis Kesoglou',
    maintainer_email='akiskesoglou@gmail.com',
    license='MIT',
    
    zip_safe=False,
    packages=[
        'emailauth',
    ],
    
    install_requires=[
        'Django >= 1.5',
    ],
    tests_require=[
        'nose',
    ],
    
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
)
