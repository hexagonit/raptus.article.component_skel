# -*- coding: utf-8 -*-
"""
Grabs the tests in doctest
"""
__docformat__ = 'restructuredtext'


from zope.testing import doctest
from zopeskel.tests.test_zopeskeldocs import ZopeSkelLayer
from zopeskel.tests.test_zopeskeldocs import ls
from zopeskel.tests.test_zopeskeldocs import paster
from zopeskel.tests.test_zopeskeldocs import testSetUp
from zopeskel.tests.test_zopeskeldocs import testTearDown

import doctest
import os
import popen2
import shutil
import sys
import tempfile
import unittest2 as unittest


current_dir = os.path.abspath(os.path.dirname(__file__))


class ComponentSkelLayer(ZopeSkelLayer):

    pass


def doc_suite(test_dir, setUp=testSetUp, tearDown=testTearDown, globs=None):
    """Returns a test suite, based on doctests found in /docs."""
    suite = []
    if globs is None:
        globs = globals()

    flags = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE |
             doctest.REPORT_ONLY_FIRST_FAILURE)

    package_dir = os.path.split(test_dir)[0]
    if package_dir not in sys.path:
        sys.path.append(package_dir)

    doctest_dir = os.path.join(package_dir, 'docs')

    # filtering files on extension
    docs = [os.path.join(doctest_dir, doc) for doc in
            os.listdir(doctest_dir) if doc.endswith('.txt')]

    for test in docs:
        suite.append(doctest.DocFileSuite(test, optionflags=flags, 
                                          globs=globs, setUp=setUp, 
                                          tearDown=tearDown,
                                          module_relative=False))

    return unittest.TestSuite(suite)


def test_suite():
    """returns the test suite"""
    suite = doc_suite(current_dir)
    suite.layer = ZopeSkelLayer
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')

