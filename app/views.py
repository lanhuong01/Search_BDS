from django.shortcuts import render, HttpResponse, get_object_or_404
from .forms import BDSform
from .models import BDS
from .filters import FilterBDS


# Create your views here.

def home(request):

	return HttpResponse('<h1>Welcome Home</h1>')

def showBDS(request):
	BDSs =BDS.objects.all()

	context = {'BDS':BDSs}
	return render(request, 'app/showBDS.html', context)

def searchBDS(request):

	BDSs = BDS.objects.all()
	filters = FilterBDS(request.GET, queryset=BDSs)

	context = {'filters': filters}

	return render(request, 'app/searchBDS.html', context)



