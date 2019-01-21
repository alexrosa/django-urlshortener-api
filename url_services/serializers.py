from rest_framework import serializers

from url_services.models import UrlShortener


class UrlShortenerSerializer(serializers.ModelSerializer):

    class Meta:
        model = UrlShortener
        fields = '__all__'
