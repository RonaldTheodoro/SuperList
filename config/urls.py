from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from apps.core import views as core_views
from apps.core import urls as core_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.index, name='index'),
    url(r'^lists/', include(core_urls)),
]
