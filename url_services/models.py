from django.db import models

'''
This class represents the database entity url_shortener
'''


class UrlShortener(models.Model):
    url_shortener_id = models.AutoField(primary_key=True)
    absolute_url = models.URLField(blank=False)
    short_url = models.URLField(blank=False)
    create_at = models.DateTimeField(auto_now_add=True)
