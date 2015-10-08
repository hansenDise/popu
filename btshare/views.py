from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext,loader

from .models import Torrent

# Create your views here.

def index(request):
	template = loader.get_template('btshare/index.html')
	list = Torrent.objects.order_by('torrentid')
	
	
	context = RequestContext(request,{'list':list})
	
	return HttpResponse(template.render(context))