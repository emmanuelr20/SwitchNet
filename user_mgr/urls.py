from django.conf.urls import url
from . import views

app_name = 'user_mgr'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create_account, name = 'register'),
    url(r'^login/$', views.log_in, name ='login'),
]