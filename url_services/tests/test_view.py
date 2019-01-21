from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from model_mommy import mommy


class UrlShortenerViewTestCase(APITestCase):

    def setUp(self):
        self.mocked_class = mommy.make_recipe('url_services.tests.recipes.url_shortener')

    def test_404_endpoint(self):
        url_ = 'test123'
        response = self.client.get(
            reverse('retrieve-url', args=[url_])
        )
        assert response.status_code == 404

    def test_get_short_url(self):
        response = self.client.get(
            reverse('retrieve-url', args=[self.mocked_class.short_url])
        )
        assert response.status_code == 200

    def test_get_url_list(self):
        response = self.client.get(
            reverse('url-list')
        )
        assert response.status_code == 200
        assert len(response.json().get('results')) == 1

