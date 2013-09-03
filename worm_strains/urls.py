from django.conf.urls import patterns, include, url
# urlpatterns is a module-level variable
urlpatterns = patterns('worm_strains.views', # first arg prefix for views
	# subsequent args are tuples: (regex, view, optional dictionary)
	url(r'^strains$', 'strains', name='strains_url'),
	url(r'^strain/(?P<name>.+)$', 'strain', name='strain_url')
)