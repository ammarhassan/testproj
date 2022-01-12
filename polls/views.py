from django.http import HttpResponse
from django.core.cache import cache
from polls.models import Visits

def index(request):

	if not cache.get('num_visits'):
		print('Cache Miss')
		cache.set('num_visits', 0)

	last_value = cache.get('num_visits')
	print('last cache value', last_value)
	cache.set('num_visits', last_value + 1)
	
	v, created = Visits.objects.get_or_create(id=1)
	print('Visits created status {}'.format(created))
	print('Visits Number', v.number)
	v.number += 1
	v.save()
	
	print('After this request, visit number', v.number)

	return HttpResponse("Hello, world. You're at the polls index. Visit Number: {} and from cache {}".format(v.number, cache.get('num_visits')))