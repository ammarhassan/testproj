from django.http import HttpResponse
from django.core.cache import cache
from polls.models import Visits

def index(request):

	if not cache.get('num_visits'):
		cache.set('num_visits', 0)

	last_value = cache.get('num_visits')
	cache.set('num_visits', last_value + 1)
	
	v, created = Visits.objects.get_or_create(id=1)
	v.number += 1
	v.save()

	print('this is new code sire')
	# print('After this request, visit number', v.number)

	return HttpResponse("Hello, world. You're at the polls index. Visit Number: {} and from cache {}".format(
		v.number, cache.get('num_visits')))
