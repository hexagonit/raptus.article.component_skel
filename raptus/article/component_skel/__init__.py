#from zopeskel.vars import var, DottedVar, StringVar, BooleanVar, TextVar
#from zopeskel.abstract_zope import VAR_ZOPE2
#from zopeskel.nested_namespace import VAR_NS2#, NestedNamespace
#from zopeskel.base import get_var
#from zopeskel.basic_namespace import BasicNamespace
#from zopeskel import abstract_zope
from zopeskel.plone_app import PloneApp


class ComponentTemplate(PloneApp):
#class ComponentTemplate(BasicNamespace):

    _template_dir = 'templates'
    summary = 'Template for creating a sample component for raptus.article.'
#    ndots = 2
#    required_templates = ['nested_namespace']
#    required_templates = ['basic_package']
    help = "This package creates a raptus.article component."
