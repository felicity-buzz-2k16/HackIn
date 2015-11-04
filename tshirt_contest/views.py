from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.http import Http404
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from tshirt_contest.models import Design,DesignForm,poll
import json
def index(request):
	keywords = {}
	if request.user.username:
		keywords.update({ 'user':request.user })
	designs = Design.objects.all()
	return_list = []
	for design in designs:
		if request.user.username:
			return_list.append((design, design.poll_set.filter(user=request.user)))
		else:
			return_list.append((design, []))
	keywords.update({ 'designs':return_list, })
	return render_to_response('tshirt_contest/index.html', keywords)

def error(request):
	keywords = {}
	if request.user.username:
		keywords.update({ 'user':request.user })
	return render_to_response('tshirt_contest/404.html', keywords)
@login_required
def upload(request):
	keywords = {}
	if request.user.username:
		keywords.update({ 'user':request.user })
	if request.method == 'POST':
		f = DesignForm(request.POST,request.FILES)
		if f.is_valid():
			designform = f.save(commit=False)
			designform.user = request.user
			designform.save()
			if request.FILES:
				designform.design = request.FILES['design']
				designform.save()
				return HttpResponseRedirect('/tshirt-contest/') 
	form = DesignForm()
	keywords.update({'form':form})
	return render(request, 'tshirt_contest/upload.html', keywords, context_instance=RequestContext(request))

def detail(request):
	keywords = {}
	return render_to_response('tshirt_contest/design.html', keywords)

def pollup(request):
	cat_id = None
	if request.method == 'GET':
		cat_id = request.GET['design_id']
	if cat_id:
		design = Design.objects.get(id=int(cat_id))
		vote = poll(user = request.user,design = design)
		vote.save()
		no_of_votes = poll.objects.filter(design = int(cat_id))
		data = str(len(no_of_votes)) + " " + "<i class=\"fa fa-thumbs-up\" >"
		print data
		return HttpResponse(data)

def polldown(request):
	cat_id = None
	if request.method == 'GET':
		cat_id = request.GET['design_id']
	if cat_id:
		vote = poll.objects.filter(design=int(cat_id)).filter(user=request.user)
		vote.delete()
		no_of_votes = poll.objects.filter(design = int(cat_id))
		data = str(len(no_of_votes)) + " " + "<i class=\"fa fa-thumbs-up\" >"
		print data
		return HttpResponse(data)