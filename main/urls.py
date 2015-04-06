from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^home/', views.home, name='home'),
    url(r'^loading/', views.loading, name='loading'),
    url(r'^house/(?P<pk>[0-9]+)', views.DetailView.as_view(), name="house_detail")
    #url(r'^house/(?P<house_id>[0-9]+)', views.DetailView.as_view(), name="house_detail")
]