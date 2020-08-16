"""mycontroller URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import reverse_lazy
from django.views.generic import RedirectView

from openwisp_controller.config.utils import get_controller_urls
from openwisp_controller.geo.utils import get_geo_urls

# from .sample_config import views as config_views
# from .sample_geo import views as geo_views

redirect_view = RedirectView.as_view(url=reverse_lazy('admin:index'))

urlpatterns = [
    # ... other urls in your project ...
    # Use only when changing controller API views (discussed below)
    # url(r'^controller/', include((get_controller_urls(config_views), 'controller'), namespace='controller'))

    # Use only when changing geo API views (discussed below)
    # url(r'^geo/', include((get_geo_urls(geo_views), 'geo'), namespace='geo'),),

    # openwisp-controller urls
    url(r'^$', redirect_view, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'', include('openwisp_controller.urls')),
    url(r'', include('openwisp_controller.config.controller.urls')),
    url(r'', include('openwisp_monitoring.urls')),
    url(r'', include('openwisp_notifications.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)