#!/usr/bin/python


from setuptools import setup, find_packages
import radiuslib

version = radiuslib.__version__

install_requires = [
    'six>=1.8.0',
    'Twisted>=13.0.0',
    'SQLAlchemy',
    'treq',
    'cyclone',
    'pycrypto'
]
install_requires_empty = []

package_data={}


setup(name='radiuslib',
      version=version,
      author='ZhangJing',
      author_email='ZhangJing@outlook.com',
      url='https://github.com/online2311/Radiuslib',
      license='MIT',
      description='radiusstruct python tools',
      long_description=open('README.md').read(),
      classifiers=[
       'Development Status :: 6 - Mature',
       'Intended Audience :: Developers',
       'Programming Language :: Python :: 2.6',
       'Programming Language :: Python :: 2.7',
       'Topic :: Software Development :: Libraries :: Python Modules',
       ],
      packages=find_packages(),
      package_data=package_data,
      keywords=['toughstruct','toughradius'],
      zip_safe=True,
      include_package_data=True,
      install_requires=install_requires,
)