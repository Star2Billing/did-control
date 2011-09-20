from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_countries import CountryField
from django_countries.fields import Country
from datetime import datetime


class DidCountry(models.Model):
    """This defines the Country list

    **Attributes**:

        * ``country_code`` - DID no.
        * ``label`` - DID label.

    """
    #country_code = models.CharField(max_length=2)
    country = CountryField()
    active = models.BooleanField(default=0)

    class Meta:
        db_table = u'did_country'
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def __unicode__(self):
        #return "%s" % (self.country)
        return "%s" % str(Country(code=self.country.name))


class Did(models.Model):
    """This defines the DID

    **Attributes**:

        * ``did`` - DID no.
        * ``label`` - DID label.
        * ``country`` - country field
        * ``active`` -
        * ``createdon`` - created date
        * ``updatedon`` - updated date

    **Relationships**:

        * ``country`` - Foreign key relationship to the DidCountry model. \
        Each DID mapped with a country

    **Name of DB table**: did
    """
    did = models.CharField(max_length=50)
    label = models.CharField(max_length=256)
    country = models.ForeignKey(DidCountry)
    active = models.BooleanField(default=0)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = u'did'
        verbose_name = _("DID")
        verbose_name_plural = _("DIDs")

    def __unicode__(self):
        return "%s - %s" % (self.id, self.did)
