#!/usr/bin/env python

# Python
import os
import sys
from distutils import sysconfig

# Setuptools
from setuptools import setup

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

relative_site_packages = os.path.relpath(sysconfig.get_python_lib(), sys.prefix)

setup(
    name='ansible-windows-compat',
    version='0.0.0',
    author='Chris Church',
    author_email='chris@ninemoreminutes.com',
    description='Compatibility library to run Ansible Python modules on a '
                'Windows target.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst'),
                          'rb').read().decode('utf-8'),
    license='BSD',
    keywords='python ansible windows',
    url='https://github.com/cchurch/ansible-windows-compat',
    packages=['ansible_windows_compat'],
    data_files=[(relative_site_packages, ['ansible_windows_compat.pth'])],
    include_package_data=False,
    zip_safe=False,
    install_requires=[],
    setup_requires=[],
    #tests_require=['six'],
    #test_suite='test_ansible_windows_compat.suite',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        #'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        #'Programming Language :: Python :: 3.2',
        #'Programming Language :: Python :: 3.3',
        #'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries',
    ],
    options={
        'egg_info': {
            'tag_build': '.dev',
        },
        'aliases': {
            'dev_build': 'egg_info sdist',
            'release_build': 'egg_info -b "" -R sdist',
        },
    },
    **extra
)
