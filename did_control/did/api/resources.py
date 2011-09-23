from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from django.contrib.auth.models import User
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.authorization import Authorization
from tastypie.serializers import Serializer
from did.models import *


class DidCountryResource(ModelResource):
    """
    **Attributes**:

        * ``country_code`` - DID no.
        * ``label`` - DID label.

    **Create**:

        CURL Usage::

            curl -u username:password --dump-header - -H "Content-Type: application/json" -X POST --data '{"country": "IN", "active": "1"}' http://localhost:8000/api/app/country/

        Response::

            HTTP/1.0 201 CREATED
            Date: Fri, 23 Sep 2011 06:08:34 GMT
            Server: WSGIServer/0.1 Python/2.7.1+
            Vary: Accept-Language, Cookie
            Content-Type: text/html; charset=utf-8
            Location: http://localhost:8000/api/app/country/1/
            Content-Language: en-us


    **Read**:

        CURL Usage::

            curl -u username:password -H 'Accept: application/json' http://localhost:8000/api/app/country/?format=json

        Response::

            {
               "meta":{
                  "limit":20,
                  "next":null,
                  "offset":0,
                  "previous":null,
                  "total_count":4
               },
               "objects":[
                  {
                     "active":true,
                     "country":"IN",
                     "id":"1",
                     "resource_uri":"/api/app/country/1/"
                  },
               ]
            }


    **Update**:

        CURL Usage::

            curl -u username:password --dump-header - -H "Content-Type: application/json" -X PUT --data '{"country": "IN", "active": 1}' http://localhost:8000/api/app/country/1/

        Response::

            HTTP/1.0 204 NO CONTENT
            Date: Fri, 23 Sep 2011 06:46:12 GMT
            Server: WSGIServer/0.1 Python/2.7.1+
            Vary: Accept-Language, Cookie
            Content-Length: 0
            Content-Type: text/html; charset=utf-8
            Content-Language: en-us


    **Delete**:

        CURL Usage::

            curl -u username:password --dump-header - -H "Content-Type: application/json" -X DELETE  http://localhost:8000/api/app/country/1/

            curl -u username:password --dump-header - -H "Content-Type: application/json" -X DELETE  http://localhost:8000/api/app/country/

        Response::

            HTTP/1.0 204 NO CONTENT
            Date: Fri, 23 Sep 2011 06:48:03 GMT
            Server: WSGIServer/0.1 Python/2.7.1+
            Vary: Accept-Language, Cookie
            Content-Length: 0
            Content-Type: text/html; charset=utf-8
            Content-Language: en-us

    **Search**:

        CURL Usage::

            curl -u username:password -H 'Accept: application/json' http://localhost:8000/api/app/country/?country=IN

        Response::

            {
               "meta":{
                  "limit":20,
                  "next":null,
                  "offset":0,
                  "previous":null,
                  "total_count":1
               },
               "objects":[
                  {
                     "active":true,
                     "country":"IN",
                     "id":"2",
                     "resource_uri":"/api/app/country/2/"
                  }
               ]
            }
    """
    class Meta:
        queryset = DidCountry.objects.all()
        resource_name = 'country'
        filtering = {
            'country': ALL,
            'active': ALL,
        }
        authorization = Authorization()
        authentication = BasicAuthentication()


class DidResource(ModelResource):
    """
    **Attributes**:

            * ``did`` - DID no.
            * ``label`` - DID label.
            * ``country`` - country field
            * ``active`` - true/false
            * ``createdon`` - created date
            * ``updatedon`` - updated date

    **Create**:

        CURL Usage::

            curl -u username:password --dump-header - -H "Content-Type: application/json" -X POST --data '{"did": "123", "label": "xyz", "country": "IN", "active": "1"}' http://localhost:8000/api/app/did/

        Response::

            HTTP/1.0 201 CREATED
            Date: Fri, 23 Sep 2011 06:08:34 GMT
            Server: WSGIServer/0.1 Python/2.7.1+
            Vary: Accept-Language, Cookie
            Content-Type: text/html; charset=utf-8
            Location: http://localhost:8000/api/app/country/1/
            Content-Language: en-us


    **Read**:

        CURL Usage::

            curl -u username:password -H 'Accept: application/json' http://localhost:8000/api/app/did/?format=json

        Response::

            {
               "meta":{
                  "limit":20,
                  "next":null,
                  "offset":0,
                  "previous":null,
                  "total_count":1
               },
               "objects":[
                  {
                     "active":true,
                     "did":"1",
                     "id":"1",
                     "label":"xyz",
                     "resource_uri":"/api/app/did/1/",
                     "createdon":"2011-09-20T07:25:23",
                     "updatedon":"2011-09-20T07:25:23"
                  }
               ]
            }


    **Update**:

        CURL Usage::

            curl -u username:password --dump-header - -H "Content-Type: application/json" -X PUT --data '{"did": "123", "label": "xyz", "country": "IN", "active": "1"}' http://localhost:8000/api/app/did/1/

        Response::

            HTTP/1.0 204 NO CONTENT
            Date: Fri, 23 Sep 2011 06:46:12 GMT
            Server: WSGIServer/0.1 Python/2.7.1+
            Vary: Accept-Language, Cookie
            Content-Length: 0
            Content-Type: text/html; charset=utf-8
            Content-Language: en-us


    **Delete**:

        CURL Usage::

            curl -u username:password --dump-header - -H "Content-Type: application/json" -X DELETE  http://localhost:8000/api/app/did/1/

            curl -u username:password --dump-header - -H "Content-Type: application/json" -X DELETE  http://localhost:8000/api/app/did/

        Response::

            HTTP/1.0 204 NO CONTENT
            Date: Fri, 23 Sep 2011 06:46:12 GMT
            Server: WSGIServer/0.1 Python/2.7.1+
            Vary: Accept-Language, Cookie
            Content-Length: 0
            Content-Type: text/html; charset=utf-8
            Content-Language: en-us


    **Search**:

        CURL Usage::

            curl -u username:password -H 'Accept: application/json' http://localhost:8000/api/app/did/?did=123

        Response::

            {
               "meta":{
                  "limit":20,
                  "next":null,
                  "offset":0,
                  "previous":null,
                  "total_count":0
               },
               "objects":[]
            }
    """
    class Meta:
        queryset = Did.objects.all()
        resource_name = 'did'
        filtering = {
            'did': ALL,
            'country': ALL,
        }
        authorization = Authorization()
        authentication = BasicAuthentication()


class UserResource(ModelResource):
    """
    ``To create``::

        curl -u username:password --dump-header - -H "Content-Type: application/json" -X POST --data '{"last_name": "Belaid", "first_name": "areski", "username": "areski", "password": "areski"}' http://localhost:8000/api/app/user/


    ``To read/get``::

        curl -u username:password -H 'Accept: application/json' http://localhost:8000/api/app/user/?format=json


    ``To update``::

        curl -u username:password --dump-header - -H "Content-Type: application/json" -X PUT --data '{"first_name": "Areski", "last_name": ""}' http://localhost:8000/api/app/user/1/


    ``To delete``::

        curl -u username:password --dump-header - -H "Content-Type: application/json" -X DELETE  http://localhost:8000/api/app/user/1/

        curl -u username:password --dump-header - -H "Content-Type: application/json" -X DELETE  http://localhost:8000/api/app/user/

    ``To search``::

        curl -u username:password -H 'Accept: application/json' http://localhost:8000/api/app/user/?username=daniel

    """
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        filtering = {
            'username': ALL,
            'date_joined': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }
        authorization = Authorization()
        authentication = BasicAuthentication()
