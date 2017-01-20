from django.conf.urls import url
from . import views

app_name = 'store_range'
urlpatterns = [
    url(r'^$', views.go_home, name='home'),
    url(r'^store/$', views.get_all, name='all'),
]