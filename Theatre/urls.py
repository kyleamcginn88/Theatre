from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from views import home, store, location, movies, performances

urlpatterns = patterns('',
    url(r'^$', home),
	url(r'^movies$', 'Theatre.views.movies', name='movies'),
	url(r'^performances$', 'Theatre.views.performances', name='performances'),
	url(r'^store$', 'Theatre.views.store', name='store'),
	url(r'^location$', 'Theatre.views.location', name='location'),
	
    url(r'^admin/', include(admin.site.urls)),
)
