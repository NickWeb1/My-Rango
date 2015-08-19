from django.conf.urls import include, url
from django.contrib import admin
from rango import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'TangoDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^rango/', include('rango.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
