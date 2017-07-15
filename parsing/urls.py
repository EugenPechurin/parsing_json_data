"""parsing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from parsing_json import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^graph/(?P<region>[\w\s-]+)/$', views.graph, name='graph'),
    url(r'^graph/$', views.graph, name='graph'),
    url(r'^delete_data/$', views.delete_data, name='delete_data'),
    url(r'^', views.parsing_json, name='parsing_json')
]

if settings.DEBUG:
    pass
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
