from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    
    url(r'logout$', 'django.contrib.auth.views.logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL}),
    url(r'^annotated(.*)$', "cms_users_put.views.plantilla"),
    url(r'^$', "cms_users_put.views.todo"),
    url(r'^page/(.*)$', "cms_users_put.views.handler"),
    url(r'(.*)$', "cms_users_put.views.notfound"),
)
