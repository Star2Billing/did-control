from django.conf.urls.defaults import *

from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from piston.doc import documentation_view
from did.api.handlers import *


class CsrfExemptResource(Resource):
    """A Custom Resource that is csrf exempt"""
    def __init__(self, handler, authentication=None):
        super(CsrfExemptResource, self).__init__(handler, authentication)
        self.csrf_exempt = getattr(self.handler, 'csrf_exempt', True)

auth = HttpBasicAuthentication(realm='DID-control Application')
did_handler = CsrfExemptResource(didHandler, authentication=auth)
didcountry_handler = CsrfExemptResource(didcountryHandler, authentication=auth)


urlpatterns = patterns('',

    url(r'^did_list[/]$', did_handler),
    url(r'^did_list/(?P<did_id>[^/]+)', did_handler),
    url(r'^country_list[/]$', didcountry_handler),
    url(r'^country_list/(?P<country_id>[^/]+)', didcountry_handler),
    # automated documentation
    url(r'^doc[/]$', documentation_view),
)
