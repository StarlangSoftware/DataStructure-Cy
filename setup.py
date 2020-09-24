from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(["DataStructure/*.pyx", "DataStructure/Cache/*.pyx", "DataStructure/Cache/*.pxd"], compiler_directives={'language_level' : "3"}),
    name='NlpToolkit-DataStructure-Cy',
    version='1.0.1',
    packages=['DataStructure', 'DataStructure.Cache'],
    url='https://github.com/olcaytaner/DataStructure-Cy',
    license='',
    author='olcaytaner',
    author_email='olcaytaner@isikun.edu.tr',
    description='Simple Data Structures Library'
)
