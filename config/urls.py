from django.conf.urls import url
from django.contrib import admin
from apps.core import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^lists/new$', views.new_list, name='new_list'),
    url(r'^lists/user-list/$', views.view_list, name='view_list'),
]
