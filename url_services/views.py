import coreapi
import coreschema
import json

from django.http import HttpResponseRedirect
from rest_framework.schemas import AutoSchema

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from url_services.services import UrlShortenerService
from url_services.serializers import UrlShortenerSerializer
from config import settings

'''
This module is responsible to the view.
'''

class UrlServicesListView(APIView):
    _service_class = UrlShortenerService

    def get(self, request):
        _service = self._service_class()
        url_list = _service.list_urls()
        if url_list:
            return Response(url_list, status=status.HTTP_200_OK)
        return Response('Internal error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UrlServicesDetailView(APIView):
    _service_class = UrlShortenerService
    schema = AutoSchema()

    def get(self, request, coded_url):
        _service = self._service_class()
        if not coded_url:
            return Response('Bad Request', status=status.HTTP_400_BAD_REQUEST)

        result = _service.retrieve(short_url=coded_url)
        serializer = UrlShortenerSerializer(result)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response('Internal error!', status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UrlServicesRedirectView(APIView):
    _service_class = UrlShortenerService
    schema = AutoSchema()

    def get(self, request, coded_url):
        _service = self._service_class()
        if not coded_url:
            return Response('Bad Request', status=status.HTTP_400_BAD_REQUEST)

        base_url = settings.BASE_URL_SERVICE+'/{}'.format(coded_url)
        result = _service.retrieve(short_url=base_url)
        if result:
            abs_url = result['absolute_url']
            print('abs_url= '+abs_url)
            return HttpResponseRedirect(abs_url)
        return Response('Internal error!', status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UrlServicesCreateView(APIView):
    media_type='application/json'
    _service_class = UrlShortenerService
    serializer_class = UrlShortenerSerializer

    schema = AutoSchema(manual_fields=[
        coreapi.Field('url', required=True, location='body', description='This method expecting a Json object like this: {"url": "www.website.com"}', schema=coreschema.String()),
    ])
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        _url = body_data['url']
        _service = self._service_class()
        result = _service.shorten_url(_url)
        return result

