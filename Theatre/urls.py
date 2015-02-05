from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from views import home, store, location, movies, performances

urlpatterns = patterns('',
    url(r'^$', home),
	url(r'^movies$', 'Theatre_CS399.views.movies', name='movies'),
	url(r'^performances$', 'Theatre_CS399.views.performances', name='performances'),
	url(r'^store$', 'Theatre_CS399.views.store', name='store'),
	url(r'^location$', 'Theatre_CS399.views.location', name='location'),
	
    url(r'^admin/', include(admin.site.urls)),
)
