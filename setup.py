"""
~~~~~~~~~~~
Zmdictalchemy
~~~~~~~~~~~

Contains asdict() and fromdict() methods that will work on SQLAlchemy
declarative models.

Read more in the source or on github
<https://github.com/dafu-wu/zmdictalchemy>.
"""

import os
import sys
from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

# Requirements for the package
install_requires = [
    'SQLAlchemy>=0.9.4',
]

# Requirement for running tests
test_requires = install_requires

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

setup(name='zmdictalchemy',
      version='0.1.2.8',
      description="Contains asdict and fromdict methods for SQL-Alchemy "
      "declarative models",
      long_description=README,
      url='http://github.com/dafu-wu/zmdictalchemy/',
      license='MIT',
      author='Dadu Wu',
      author_email='wucy4328@gmail.com',
      platforms='any',
      classifiers=['Development Status :: 4 - Beta',
                   'License :: OSI Approved :: MIT License',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                   'Topic :: Software Development :: '
                   'Libraries :: Python Modules'],
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=test_requires,
      test_suite='zmdictalchemy',
      **extra)
