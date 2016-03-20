from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'comodo'

urlpatterns = [
    url(r'^$',views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^post_edit/(?P<pk>\d+)/', views.EditPostView.as_view(), name='post_edit'),
    url(r'^post_create/$', views.CreatePostView.as_view(), name='post_create'),
    url(r'^registers/$', views.register, name='registers'),
    url(r'^accounts/login/$',
    auth_views.login,
    {'template_name': 'login.html'},
    name='auth_login'),
    url(r'^logout/$',
    auth_views.logout,
    {'template_name': 'registration/logout.html'},
    name='auth_logout'),
    url(r'^password/change/$',
    auth_views.password_change,
    name='auth_password_change'),
url(r'^password/change/done/$',
    auth_views.password_change_done,
    name='password_change_done'),
url(r'^password/reset/$',
    auth_views.password_reset,
    name='auth_password_reset'),
url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    auth_views.password_reset_confirm,
    name='auth_password_reset_confirm'),
url(r'^password/reset/complete/$',
    auth_views.password_reset_complete,
    name='auth_password_reset_complete'),
url(r'^password/reset/done/$',
    auth_views.password_reset_done,
    name='password_reset_done'),

]