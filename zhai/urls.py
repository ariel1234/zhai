from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('main.urls', namespace="main")),
    url(r'^admin/', include(admin.site.urls)),
]
