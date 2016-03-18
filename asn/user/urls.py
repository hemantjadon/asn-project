from django.conf.urls import url,include
from user import views

urlpatterns = [
	url(r'^$', views.UserList.as_view(),name='user-list'),
    url(r'^create/$',views.UserCreate.as_view(),name='user-create'),
	url(r'^(?P<pk>[0-9]+)/$', views.UserRetrieve.as_view(),name='user-detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.UserUpdate.as_view(),name='user-update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.UserDelete.as_view(),name='user-delete'),
]