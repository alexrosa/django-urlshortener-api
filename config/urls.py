from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from rest_framework_swagger.views import get_swagger_view
from url_services.views import (UrlServicesRedirectView, UrlServicesListView,
                                UrlServicesCreateView, UrlServicesDetailView)

schema_view = get_swagger_view(title='URL Shortener API')

urlpatterns = [
    path('', RedirectView.as_view(url='docs/')),
    path('docs/', schema_view),
    path('short/manager/list',UrlServicesListView.as_view(), name='url-list'),
    path('short/manager/create',UrlServicesCreateView.as_view(), name='create-url'),
    path('short/manager/<str:coded_url>', UrlServicesDetailView.as_view(), name='retrieve-url'),
    path('short/<str:coded_url>', UrlServicesRedirectView.as_view(), name='url-shortened'),
    path('', admin.site.urls),
]
