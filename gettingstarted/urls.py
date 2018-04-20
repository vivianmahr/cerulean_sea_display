from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import c_sea_dir.views

urlpatterns = [
    url(r'^$', c_sea_dir.views.index, name='index'),
    url(r'^process_sentence/$', c_sea_dir.views.process_sentence, name='process_sentence'),
    path('admin/', admin.site.urls),
]
