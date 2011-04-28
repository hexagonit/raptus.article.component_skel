from setuptools import setup, find_packages
import os

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = read('raptus', 'article', 'component_skel', 'version.txt')[:-1]

setup(name='raptus.article.component_skel',
      version=version,
      description="raptus.article component skeleton",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read() + "\n" +
                       open(os.path.join("docs", "CONTRIBUTORS.txt")).read() + "\n" +
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
      url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['raptus', 'raptus.article'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'Cheetah<=2.2.1',
          'Paste',
          'PasteScript',
          'ZopeSkel',
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      [paste.paster_create_template]
      raptus_article_component = raptus.article.component_skel:ComponentTemplate

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
