from django.urls import path, include, re_path
from django.views.generic import RedirectView
from django.contrib.staticfiles.views import serve

from .api import DataList, RefreshData

urlpatterns = [
    path('', serve, kwargs={'path': 'index.html'}),
    re_path(r'^(?!/?static/)(?!/?media/)(?P<path>.*\..*)$',
    RedirectView.as_view(url='/static/%(path)s', permanent=False)),
]

api_urls = [
    path('fetch_data/', DataList.as_view(), name='fetch-data'),
    path('refresh_data/', RefreshData.as_view(), name='refresh-data')
]

urlpatterns.extend([
    path('api/', include(api_urls)),
])
