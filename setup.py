from setuptools import setup, find_packages
import os

version = '0.1.0'

setup(name='raptus.article.component_skel',
      version=version,
      description="raptus.article component skeleton",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read() + "\n" +
                       open(os.path.join("docs", "CREDITS.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Hexagon IT',
      author_email='oss@hexagonit.fi',
      url='git',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['raptus', 'raptus.article'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'paste',
          'pastescript',
          'Cheetah<=2.2.1',
          'ZopeSkel',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      [paste.paster_create_template]
      raptus_article_component = raptus.article.component_skel:ComponentTemplate

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
