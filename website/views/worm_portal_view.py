from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

@login_required
def worm_portal(request):
	"""
	Worm Portal landing page
	"""
	# render page
	return render_to_response('worm_portal.html', context_instance=RequestContext(request))
