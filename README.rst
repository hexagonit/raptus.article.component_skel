Introduction
============

raptus.article.component_skel creates component skeleton for raptus.article.

You may want to read:

* `raptus.article.core`_

.. _raptus.article.core: http://plone.org/products/raptus.article.core

Register raptus_article_component to paster template
====================================================

``easy_install`` the package::

    easy_install raptus.article.component_skel

Now ``raptus_article_component`` is added to the paster template.

Check if the template is added::

    paster create --list-templates

You should see something like::

    ...
    plone_app:                 A project for Plone products with a nested namespace (2 dots in name)
    plone_hosting:             Plone hosting: buildout with ZEO and Plone versions below 3.2
    plone_pas:                 A project for a Plone PAS plugin
    raptus_article_component:  Template for creating a sample component for raptus.article.
    recipe:                    A recipe project for zc.buildout
    silva_buildout:            A buildout for Silva projects
    ...

Creating your_component
=======================

Under ``src`` directory, do something like::

    paster create -t raptus_article_component raptus.article.your_component

Running the command above creates package named raptus.article.your_component with the next structure::

    raptus.article.your_component/
    |-- README.txt
    |-- docs
    |   |-- CREDITS.txt
    |   |-- HISTORY.txt
    |   |-- LICENSE.GPL
    |   `-- LICENSE.txt
    |-- raptus
    |   |-- __init__.py
    |   `-- article
    |       |-- __init__.py
    |       `-- your_component
    |           |-- __init__.py
    |           |-- browser
    |           |   |-- __init__.py
    |           |   |-- component.py
    |           |   |-- configure.zcml
    |           |   `-- viewlets
    |           |       `-- component.pt
    |           |-- configure.zcml
    |           |-- locales
    |           |   `-- raptus.article.your_component.pot
    |           |-- profile
    |           |   |-- default
    |           |      `-- metadata.xml
    |           `-- version.txt
    `-- setup.py

Once you have created the new component package, add the next line to your buildout.cfg file::

    eggs =
        ...
        raptus.article.your_component
        ...

    develop =
        ...
        src/raptus.article.your_component
        ...

Now run the next command::

    ./bin/buildout

Once you have successfully run buildout command, test if the package is correctly created.

For Plone4::

    ./bin/test -s raptus.article.your_component

For Plone3::

    ./bin/instance test -s raptus.article.your_component

The result would be something like::

    Ran 4 tests with 0 failures and 0 errors in 2.177 seconds.

Now if you want to see how it workd in the real plone site, just quickinstall your component and go to Article logged in with user who can edit the article.

* If you do not know how to install products, `Installing Add-ons`_ may help.

.. _Installing Add-ons: http://plone.org/documentation/kb/add-ons/installing

From the Component tab, you must see your_component.

Check the component and save.

Then click View.

There should be ``Sample Viewlet`` text in the page.
This is the viewlet you have applied to this article.


How To Customize Component
==========================

Component
---------

You need to open ``component.py`` file under browser directory and edit Component class.

Component class::

    class Component(object):
        """ The Simple Component
        """
        implements(IComponent)
        adapts(IArticle)
        
        title = _("Sample Component")
        description = _("Description of Sample Component")
        image = '++resource++sample.gif'
        interface = IMarker
        viewlet = 'raptus.article.your_component'

        def __init__(self, context):
            self.context = context

* IMarker is a marker interface which inherits zope.interface.Interface.
* This Component class takes context (article) to initialize it.
* title, description and image will be shown in the Article Components tab.
* viewlet is the name which will be shown in the Article View.

Viewlet
-------

Viewlet class::

    class ComponentViewlet(ViewletBase):
        """ Viewlet to be displayed on View.
        """
        index = ViewPageTemplateFile('viewlets/component.pt')

* Simply renders component.pt to the article.

Component Registration
----------------------

browser/configure.zcml::

    <configure
        xmlns="http://namespaces.zope.org/zope"
        xmlns:browser="http://namespaces.zope.org/browser"
        xmlns:article="http://namespaces.zope.org/article">

      <include package="raptus.article.core" />

      <article:component
          name="your_component"
          component=".component.Component"
          viewlet="raptus.article.your_component.browser.component.ComponentViewlet"
          manager="plone.app.layout.viewlets.interfaces.IBelowContentBody"
          />

    </configure>

<include package="raptus.article.core" /> is important here since without this, 
you get::

    Error: ConfigurationError: ('Unknown directive', u'http://namespaces.zope.org/article', u'component')

Now the component named "your_component" is registered with component class ".component.Component", which then uses viewlet ".component.ComponentViewlet" in viewlet manager "plone.app.layout.viewlets.interfaces.IBelowContentBody".
