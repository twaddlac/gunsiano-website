from django.template import RequestContext # extends Context; needed for STATIC_URL
from django.shortcuts import render_to_response, get_object_or_404 # r_to_r loads template, passes c    ontext, renders
from worm_strains.models import *

def strains(request):
	"""
	Page listing worms strains, with possible filtering
	"""
	# get all worm strains
	strains = WormStrain.objects.all().order_by('strain_sort')	
	
	"""
	The following, commented out, would dynamically generate genotypes 
	when they can be created from the background and a single transgene.
	For performance, all genotypes are instead hard-coded into the database,
	using the generate_genotype function in this module along with
	the script worm_strains/management/commands/insert_genotypes_into_database.py
	(which can be run with "python manage.py insert_genotypes_into_database").
	"""
	"""
	for strain in strains:
		generate_genotype(strain)
	
	"""

	# render page
	return render_to_response('strains.html', {
		'strains':strains
	}, context_instance=RequestContext(request))


def generate_genotype(strain):
	if strain.transgene and strain.parent_strain:
		vector = strain.transgene.vector
		strain.genotype = strain.transgene.name + "[" + vector.parent_vector.genotype_pattern + "]"
		strain.genotype = strain.genotype.replace("gene", vector.gene)
		strain.genotype = strain.genotype.replace("promoter", vector.promoter)
		strain.genotype = strain.genotype.replace("threePrimeUTR", vector.three_prime_utr)
		if strain.parent_strain.name == "DP38":
			strain.genotype = "unc-119(ed3) III; " + strain.genotype
