from django.conf.urls import url,include
from blogs import views

urlpatterns = [
	url(r'^$', views.BlogList.as_view(),name='blog-list'),
    url(r'^create/$',views.BlogCreate.as_view(),name='blog-create'),
	url(r'^(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', views.BlogDetail.as_view(),name='blog-detail'),
    url(r'^(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/update/$', views.BlogUpdate.as_view(),name='blog-update'),
    url(r'^(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/delete/$', views.BlogDelete.as_view(),name='blog-delete'),
    
    url(r'^(?P<blogID>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/comment/$', views.BlogCommentList.as_view(),name='blog-comment-list'),
    url(r'^comment/create/$',views.BlogCommentCreate.as_view(),name='blog-comment-create'),
	url(r'^(?P<blogID>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/comment/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', views.BlogCommentDetail.as_view(),name='blog-comment-detail'),
    url(r'^(?P<blogID>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/comment/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/update/$', views.BlogCommentUpdate.as_view(),name='blog-comment-update'),
    url(r'^(?P<blogID>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/comment/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/delete/$', views.BlogCommentDelete.as_view(),name='blog-comment-delete'),
]