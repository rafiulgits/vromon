from django.test import TestCase

lat1 = 23.734354
lng1 = 90.415480


l = [{'lat':23.738125, 'lng':90.387446},
	{'lat':23.734325, 'lng':90.391246},
	{'lat':23.745725, 'lng':90.395446},
	{'lat':23.738112, 'lng':90.405146},
	{'lat':23.738905, 'lng':90.395446},
	{'lat':23.738125, 'lng':90.391246}]



for i in l:
	print(abs(lat1-i['lat']), abs(lng1-i['lng']))


