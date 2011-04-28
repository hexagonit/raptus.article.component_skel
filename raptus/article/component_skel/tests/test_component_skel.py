from raptus.article.component_skel import ComponentTemplate
from zopeskel.plone_app import PloneApp

import unittest2 as unittest


class test_component_skel(unittest.TestCase):
    """ test for methods on the base template class
    """

    def test_ComponentTemplate_subclass_of_PloneApp(self):
        self.failUnless(issubclass(ComponentTemplate, PloneApp))

    def test_ComponentTemplate(self):
        template = ComponentTemplate('id')
        self.assertEqual('templates', template._template_dir)
        self.assertEqual('Template for creating a sample component for raptus.article.', template.summary)
        self.assertEqual('This package creates a raptus.article component.', template.help)


def test_suite():
    suite = unittest.TestSuite([
        unittest.makeSuite(test_component_skel)])
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
