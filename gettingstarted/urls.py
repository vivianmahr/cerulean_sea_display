from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import c_sea_dir.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', c_sea_dir.views.index, name='index'),
    url(r'^db', c_sea_dir.views.db, name='db'),
    path('admin/', admin.site.urls),
]
