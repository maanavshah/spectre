from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^spectre/$', views.reviews, name='reviews'),
    url(r'^spectre/login/$',views.login, name='login'),
    url(r'^spectre/register/$',views.register, name='register'),
    url(r'^spectre/reviews/post/(?P<pk>\d+)/$', views.review, name='review'),
    url(r'^spectre/reviews/add/$',views.add_review, name='add_reviews'),
    url(r'^spectre/reviews/edit/(?P<pk>\d+)/$', views.reviews_edit, name='reviews_edit'),
    url(r'^spectre/about/$',views.about, name='about'),
    url(r'^spectre/logout/$',views.logout, name='logout'),
    url(r'^spectre/reviews/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
 	url(r'^hits/$',views.hits, name='hits')   
]
