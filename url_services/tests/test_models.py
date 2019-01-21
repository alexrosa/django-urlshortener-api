from datetime import datetime

from django.test import TestCase
from model_mommy import mommy
from url_services.models import UrlShortener


class UrlShortenerTestCase(TestCase):

    def setUp(self):
        self.mocked_class = mommy.make_recipe('url_services.tests.recipes.url_shortener')

    def test_get_url_shortened(self):
        url_shortened = UrlShortener.objects.get(short_url__exact=self.mocked_class.short_url)
        assert url_shortened is not None

    def test_list_reservation(self):
        urls = list(UrlShortener.objects.all())
        assert len(urls) >= 1