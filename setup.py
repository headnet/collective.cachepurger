from setuptools import setup, find_packages
import os

version = '1.1'

setup(name='collective.cachepurger',
      version=version,
      description="Purges RAM caches and refreshes resource registry",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Anton Stonor',
      author_email='anton@headnet.dk',
      url='https://github.com/headnet/collective.cachepurger',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
