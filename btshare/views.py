from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext,loader
from django.shortcuts import render_to_response

from .models import Torrent

# Create your views here.

def index(request):
	template = loader.get_template('btshare/index.html')
	list = Torrent.objects.order_by('torrentid')
	
	
	context = RequestContext(request,{'list':list})
	
	return HttpResponse(template.render(context))
	
def doit(request):
	return HttpResponse("just do it!")
	
def torrent_detail(request,torrentid):
	
	return render_to_response('btshare/torrentdetail.html',{'torrentid':torrentid,'posterurl':'65b063cd36bfe1da3a13a867b8387b179bcf9f8a','screenurl1':'cc36f436ed228010996e2d0610797a6208a56f9c','screenurl2':'a830789c0714207205b20edab4e2e60b1bbc65a2'})