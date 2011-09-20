from piston.handler import BaseHandler
from piston.emitters import *
from piston.utils import rc, require_mime, require_extended, throttle
from did.models import *
from django.db import IntegrityError
from django.db.models import Q
import time

#TODO make sure we get int for ID settings


def get_attribute(attrs, attr_name):
    """This is a helper to retrieve an attribute if it exists"""
    if attr_name in attrs:
        attr_value = attrs[attr_name]
    else:
        attr_value = None
    return attr_value


def save_if_set(record, fproperty, value):
    """function to save a property if it has been set"""
    if value:
        record.__dict__[fproperty] = value


def get_value_if_none(x, value):
    """return value if x is None"""
    if x is None:
        return value
    return x


class didHandler(BaseHandler):
    """This API provides DID management giving basic functions
    to create and read DIDs."""
    model = Did
    allowed_methods = ('POST', 'GET', 'PUT', 'DELETE')
    fields = ('id', 'did', 'label', 'country')

    def create(self, request):
        """API to create a new DID

        **Attributes**:

            * ``did`` - DID no.
            * ``label`` - DID label.
            * ``country`` - country field
            * ``active`` -
            * ``createdon`` - created date
            * ``updatedon`` - updated date

        **CURL Usage**::

            curl -u username:password -i -H "Accept: application/json" -X POST http://127.0.0.1:8000/api/did/did_list/ -d "did=2&label=xyz&country=IN&active=1"

        **Example Response**::

            {
                "did": "1",
                "country": "IN",
                "id": 1,
                "label": "Sample DID"
            }

        """
        attrs = self.flatten_dict(request.POST)

        did = get_attribute(attrs, 'did')
        label = get_attribute(attrs, 'label')
        country = get_attribute(attrs, 'country')
        active = get_attribute(attrs, 'active')
        
        try:
            new_did = Did.objects.create(did=did,
                                         label=label,
                                         country=country,
                                         active=active)
        except IntegrityError:
            #raise
            resp = rc.BAD_REQUEST
            resp.write("Error adding DID!")
            return resp

        return new_did

    @throttle(1000, 1 * 60) #  Throttle if more that 1000 times within 1 minute
    def read(self, request, did_id=None):
        """API to read all created DIDs, or a specific Did\
        if a did_id is supplied

        **Attributes**:

            * ``did_id`` - Did ID

        **CURL Usage**::

            curl -u username:password -i -H "Accept: application/json" -X GET http://127.0.0.1:8000/api/did/did_list/

            curl -u username:password -i -H "Accept: application/json" -X GET http://127.0.0.1:8000/api/did/did_list/%did_id%/

        **Example Response**::

            {
                "did": "1",
                "country": "IN",
                "id": 1,
                "label": "Sample DID"
            }

        **Error**:

            * DID not found
        """
        base = Did.objects
        if did_id:
            try:
                list_did = base.get(id=did_id)
                return list_did
            except:
                return rc.NOT_FOUND
        else:
            return base.all().order_by('-id')[:10]


    @throttle(1000, 1 * 60) #  allow 1000 times in 1 minutes
    def update(self, request, did_id=None):
        """API to update a did

        **Attributes**:

            * ``did`` - DID no.
            * ``label`` - DID label.
            * ``country`` - country field
            * ``active`` -
            * ``createdon`` - created date
            * ``updatedon`` - updated date

        **CURL Usage**::

            curl -u username:password -i -H "Accept: application/json" -X PUT http://127.0.0.1:8000/api/did/did_list/%did_id%/ -d "did=2&label=xyz&country=IN&active=1"

        **Example Response**::

            {
                "did": "2",
                "country": "IN",
                "id": 2,
                "label": "xy"
            }

        **Error**:

            * DID is not found
        """
        #Retrieve Post settings
        attrs = self.flatten_dict(request.POST)
        
        did = get_attribute(attrs, 'did')
        label = get_attribute(attrs, 'label')
        country = get_attribute(attrs, 'country')
        active = get_attribute(attrs, 'active')

        try:
            obj_did = Did.objects.get(id=did_id)
            save_if_set(obj_did, 'did', did)
            save_if_set(obj_did, 'label', label)
            save_if_set(obj_did, 'country', country)
            save_if_set(obj_did, 'active', active)
            obj_did.save()
            return obj_did
        except:
            return rc.NOT_FOUND

    @throttle(100, 1 * 60) # allow 100 times in 1 minutes
    def delete(self, request, did_id):
        """API to delete DID

        **Attributes**:

            * ``did_id`` - DID

        **CURL Usage**::

            curl -u username:password -i -H "Accept: application/json" -X DELETE http://127.0.0.1:8000/api/did/did_list/%did_id%/

        **Example Response**::

            HTTP/1.0 204 NO CONTENT
            Date: Wed, 18 May 2011 13:23:14 GMT
            Server: WSGIServer/0.1 Python/2.6.2
            Vary: Authorization
            Content-Length: 0
            Content-Type: text/plain

        **Error**:

            * NOT FOUND DID ID doesn't exist.
        """
        try:
            did = Did.objects.get(id=did_id)
            did.delete()
            resp = rc.DELETED
            resp.write(" DID is deleted")
            return resp
        except:
            resp = rc.NOT_FOUND
            resp.write(" DID doesn't exist")
            return resp


class didcountryHandler(BaseHandler):
    """This API provides Country management giving basic functions
    to create and read counties for DIDs."""
    model = DidCountry
    allowed_methods = ('POST', 'GET', 'PUT', 'DELETE')

    def create(self, request):
        """API to create a new country

        **Attributes**:

            * ``country`` - country field (max_chars=2)
            * ``active`` -

        **CURL Usage**::

            curl -u username:password -i -H "Accept: application/json" -X POST http://127.0.0.1:8000/api/did/country_list/ -d "country=IN&active=1"

        **Example Response**::

            {
                "active": true,
                "country": "IN"
            }
        """
        attrs = self.flatten_dict(request.POST)

        country = get_attribute(attrs, 'country')
        active = get_attribute(attrs, 'active')

        try:
            did_country = DidCountry.objects.create(country=country, active=active)
        except IntegrityError:
            #raise
            resp = rc.BAD_REQUEST
            resp.write("Error adding Country!")
            return resp

        return did_country

    @throttle(1000, 1 * 60) #  Throttle if more that 1000 times within 1 minute
    def read(self, request, country_id=None):
        """API to read all created countries, or a specific country\
        if a country_id is supplied

        **Attributes**:

            * ``country_id`` - Country ID

        **CURL Usage**::

            curl -u username:password -i -H "Accept: application/json" -X GET http://127.0.0.1:8000/api/did/country_list/

            curl -u username:password -i -H "Accept: application/json" -X GET http://127.0.0.1:8000/api/did/country_list/%country_id%/

        **Example Response**::

            {
                "active": true,
                "country": "IN"
            }

        **Error**:

            * Country not found
        """
        base = DidCountry.objects
        if country_id:
            try:
                list_country = base.get(id=country_id)
                return list_country
            except:
                return rc.NOT_FOUND
        else:
            return base.all().order_by('-id')[:10]


    @throttle(1000, 1 * 60) #  allow 1000 times in 1 minutes
    def update(self, request, country_id=None):
        """API to update a Country

        **Attributes**:

            * ``country`` - country field
            * ``active`` -

        **CURL Usage**::

            curl -u username:password -i -H "Accept: application/json" -X PUT http://127.0.0.1:8000/api/did/country_list/%country_id%/ -d "country=IN&active=1"

        **Example Response**::

            {
                "country": "IN",
                "id": 2,
                "active": "1"
            }

        **Error**:

            * Country is not found
        """
        #Retrieve Post settings
        attrs = self.flatten_dict(request.POST)

        country = get_attribute(attrs, 'country')
        active = get_attribute(attrs, 'active')

        try:
            obj_didcountry = DidCountry.objects.get(id=country_id)
            save_if_set(obj_didcountry, 'country', country)
            save_if_set(obj_didcountry, 'active', active)
            obj_didcountry.save()
            return obj_didcountry
        except:
            return rc.NOT_FOUND

    @throttle(100, 1 * 60) # allow 100 times in 1 minutes
    def delete(self, request, country_id):
        """API to delete Country

        **Attributes**:

            * ``country_id`` - Country ID

        **CURL Usage**::

            curl -u username:password -i -H "Accept: application/json" -X DELETE http://127.0.0.1:8000/api/did/country_list/%country_id%/

        **Example Response**::

            HTTP/1.0 204 NO CONTENT
            Date: Wed, 18 May 2011 13:23:14 GMT
            Server: WSGIServer/0.1 Python/2.6.2
            Vary: Authorization
            Content-Length: 0
            Content-Type: text/plain

        **Error**:

            * NOT FOUND Country ID doesn't exist.
        """
        try:
            didcountry = DidCountry.objects.get(id=country_id)
            didcountry.delete()
            resp = rc.DELETED
            resp.write(" Country is deleted")
            return resp
        except:
            resp = rc.NOT_FOUND
            resp.write(" Country doesn't exist")
            return resp
