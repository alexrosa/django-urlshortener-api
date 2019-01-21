import short_url

from urllib.parse import urlparse

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Max

from config import settings
from url_services.serializers import UrlShortenerSerializer
from url_services.models import UrlShortener


class UrlShortenerService:

    def shorten_url(self, url_to_shorten):

        if not self._is_valid_url(url_to_shorten):
            return JsonResponse({'return': 'Malformed URL'}, status=406)
        next_id = self.get_next_id()
        shortened_url = settings.BASE_URL_SERVICE+'/{}'.format(short_url.encode(next_id))
        new_url = UrlShortener(absolute_url=url_to_shorten, short_url=shortened_url)
        new_url.save()
        serializer = UrlShortenerSerializer(new_url)
        return JsonResponse({'return': serializer.data}, status=200)

    @staticmethod
    def _is_valid_url(url_to_validated):

        if not url_to_validated.startswith('htttp://'):
            url_to_validated = 'http://'+url_to_validated

        try:
            print(url_to_validated)
            result = urlparse(url_to_validated)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False

    def list_urls(self):
        queryset = UrlShortener.objects.all()
        serializer = UrlShortenerSerializer(queryset, many=True)
        return {'results': serializer.data}

    def retrieve(self, **kwargs):
        queryset = UrlShortener.objects.all()
        url_obj = get_object_or_404(queryset, **kwargs)
        serializer = UrlShortenerSerializer(url_obj)
        return serializer.data

    def get_next_id(self):
        max_id = UrlShortener.objects.all().aggregate(Max('url_shortener_id'))['url_shortener_id__max']
        return max_id + 1
