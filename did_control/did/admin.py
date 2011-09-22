from django.contrib import admin
from django.contrib import messages
from django.conf.urls.defaults import *
from django.utils.translation import ugettext as _
from django.db.models import *
from did.models import *


class DidCountryAdmin(admin.ModelAdmin):
    """Allows the administrator to view and modify certain attributes
    of a DID."""
    list_display = ('id', 'country', 'active')
    list_filter = ['active']
    ordering = ('id', )
admin.site.register(DidCountry, DidCountryAdmin)


class DidAdmin(admin.ModelAdmin):
    """Allows the administrator to view and modify certain attributes
    of a DID."""
    list_display = ('id', 'did', 'active', 'country')
    list_filter = ['active']
    ordering = ('id', )
admin.site.register(Did, DidAdmin)
