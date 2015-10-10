from django.conf.urls import patterns,include,url
import views

urlpatterns = patterns('',
	url(r'^$',views.index),
	url(r'^justdoit/$',views.doit),
	url(r'^torrent/(\d+)/$',views.torrent_detail),
)