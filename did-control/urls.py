from django.conf.urls.defaults import handler404, handler500, include,\
     patterns, url
from django.conf import settings
from django.conf.urls.i18n import *
from tastypie.api import Api
from did.api.resources import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# tastypie api
tastypie_api = Api(api_name='app')
tastypie_api.register(DidCountryResource())
tastypie_api.register(DidResource())
tastypie_api.register(UserResource())


urlpatterns = patterns('',
    # redirect
    #('^$', 'django.views.generic.simple.redirect_to',
    #{'url': '/dialer_campaign/'}),

    # Example:

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    (r'^api/did/', include('did.api.urls')),

    (r'^i18n/', include('django.conf.urls.i18n')),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),

    (r'^api/', include(tastypie_api.urls)),

)

handler404 = 'urls.custom_404_view'
handler500 = 'urls.custom_500_view'


def custom_404_view(request, template_name='404.html'):
    """404 error handler which includes ``request`` in the context.

    Templates: `404.html`
    Context: None
    """
    from django.template import Context, loader
    from django.http import HttpResponseServerError

    t = loader.get_template('404.html')  # Need to create a 404.html template.
    return HttpResponseServerError(t.render(Context({
        'request': request,
    })))


def custom_500_view(request, template_name='500.html'):
    """500 error handler which includes ``request`` in the context.

    Templates: `500.html`
    Context: None
    """
    from django.template import Context, loader
    from django.http import HttpResponseServerError

    t = loader.get_template('500.html')  # Need to create a 500.html template.
    return HttpResponseServerError(t.render(Context({
        'request': request,
    })))
