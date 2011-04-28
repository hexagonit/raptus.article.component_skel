#try:
#    from Zope2.App import zcml
#except ImportError:
#    from Products.Five import zcml
#from Products.Five import fiveconfigure
from Testing import ZopeTestCase as ztc
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup

@onsetup
def setup_product():

#    fiveconfigure.debug_mode = True
#    import raptus.article.core
#    zcml.load_config('configure.zcml', raptus.article.core)
#    import raptus.article.cart
#    zcml.load_config('configure.zcml', raptus.article.cart)
#    import collective.cart.core
#    zcml.load_config('configure.zcml', collective.cart.core)
#    import collective.cart.shipping
#    zcml.load_config('configure.zcml', collective.cart.shipping)
#    fiveconfigure.debug_mode = False

#    ztc.installPackage('raptus.article.core')
#    ztc.installPackage('raptus.article.cart')
#    ztc.installPackage('collective.cart.core')
#    ztc.installPackage('collective.cart.shipping')
    

#setup_product()
#ptc.setupPloneSite(products=['raptus.article.core', 'raptus.article.cart', 'collective.cart.core', 'collective.cart.shipping'])

class TestCase(ptc.PloneTestCase):
    """We use this base class for all the tests in this package. If
    necessary, we can put common utility or setup code in here. This
    applies to unit test cases.
    """


class FunctionalTestCase(ptc.FunctionalTestCase):
    """We use this class for functional integration tests that use
    doctest syntax. Again, we can put basic common utility or setup
    code in here.
    """
