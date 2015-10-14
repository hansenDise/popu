from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext,loader
from django.shortcuts import render_to_response
from .models import Torrent
from .models import ScreenShot
from django.db import connection

# Create your views here.

def index(request):
	#template = loader.get_template('btshare/index.html')
	#list = Torrent.objects.order_by('torrentid')
	#context = RequestContext(request,{'list':list})
	
	btlist = Torrent.objects.order_by('-addedtime')
	pages = range(1,btlist.__len__())
	return render_to_response('btshare/index.html',{'btlist':btlist,'pages':pages,'movie_inc':btlist.__len__()})
	
	#return HttpResponse(template.render(context))
	
def doit(request):
	return HttpResponse("just do it!")
	
def torrent_detail(request,torrentid):
	btitem = Torrent.objects.get(torrentid=torrentid)
	movie = btitem.movieid
	screenurl = ScreenShot.objects.filter(torrentid=torrentid)
	return render_to_response('btshare/torrentdetail.html',{'btitem':btitem,'movie':movie,'screenurl':screenurl})