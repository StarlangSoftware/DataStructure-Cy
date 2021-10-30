from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(["DataStructure/*.pyx", "DataStructure/Cache/*.pyx", "DataStructure/Cache/*.pxd"], compiler_directives={'language_level' : "3"}),
    name='NlpToolkit-DataStructure-Cy',
    version='1.0.6',
    packages=['DataStructure', 'DataStructure.Cache'],
    package_data={'DataStructure': ['*.pxd', '*.pyx', '*.c'], 'DataStructure.Cache': ['*.pxd', '*.pyx', '*.c']},
    url='https://github.com/StarlangSoftware/DataStructure-Cy',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Simple Data Structures Library',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
