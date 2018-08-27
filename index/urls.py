from .views import *


from django.conf.urls import url

urlpatterns = [
    url(r'^$', index_views),
    url(r'^home/$', home, name="blog_home"),
    url(r'^post/(?P<id>\d+)/$', Detail, name="blog_detail"),
]