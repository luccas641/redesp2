from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    #url(r'^game$', hello.views.index, name='index'),
    #url(r'^auth', hello.views.auth, name='auth'),
    #url(r'^postChoice', hello.views.postChoice, name='postChoice'),
    #url(r'^getChoice', hello.views.getChoice, name='getChoice'),
    #url(r'^new', hello.views.new, name='new'),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', hello.views.index, name='index'),
    url(r'^auth$', hello.views.auth, name='auth'),
    url(r'^sendMsg$', hello.views.send, name='send'),
    url(r'^getMsg$', hello.views.get, name='get'),
]
