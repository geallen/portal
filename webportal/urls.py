from django.conf.urls import url
from . import views

app_name =  'webportal'

urlpatterns = [
    url(r'^$', views.WebportalView.as_view(), name='webportal'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
]
