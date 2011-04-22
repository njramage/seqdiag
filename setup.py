# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os, sys

sys.path.insert(0, 'src')
import seqdiag

long_description = \
        open(os.path.join("src","README.txt")).read() + \
        open(os.path.join("src","TODO.txt")).read()

classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: System Administrators",
    "License :: OSI Approved :: Python Software Foundation License",
    "Programming Language :: Python",
    "Topic :: Software Development",
    "Topic :: Software Development :: Documentation",
    "Topic :: Text Processing :: Markup",
]

setup(
     name='seqdiag',
     version=seqdiag.__version__,
     description='seqdiag generate sequence-diagram image file from spec-text file.',
     long_description=long_description,
     classifiers=classifiers,
     keywords=['diagram','generator'],
     author='Takeshi Komiya',
     author_email='i.tkomiya at gmail.com',
     url='https://bitbucket.org/tk0miya/seqdiag',
     license='PSF',
     py_modules=['sphinxcontrib_seqdiag'],
     packages=find_packages('src'),
     package_dir={'': 'src'},
     package_data = {'': ['buildout.cfg']},
     include_package_data=True,
     install_requires=[
        'setuptools',
        'PIL',
        'blockdiag>=0.6.7',
        'funcparserlib',
         # -*- Extra requirements: -*-
     ],
     extras_require=dict(
         test=[
             'Nose',
             'minimock',
             'pep8',
         ],
     ),
     test_suite='nose.collector',
     tests_require=['Nose','minimock','pep8'],
     entry_points="""
        [console_scripts]
        seqdiag = seqdiag.command:main
     """,
)
