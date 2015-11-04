from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from gordian_knot.models import Question, Profile
from django.core.context_processors import csrf

def index(request):
	keys = { 'user':request.user }
	return render(request, 'gordian_knot/index.html')


@login_required(login_url='/buzz/portal/accounts/login/')
def score_value(request):
	return 100   # we will decrease score according to mindset of cordinators
 
@login_required(login_url='/buzz/portal/accounts/login/')
def get_started(request):
	if request.user.username:
		profile=Profile(user=request.user,score=0,tries=0,level=1)
		profile.save()
		return HttpResponseRedirect('/buzz/portal/gordian-knot/ques/1/')

@login_required(login_url='/buzz/portal/accounts/login/')   #if conditions can be removed by usign decorators
def ques(request, ques_num):
	if int(ques_num) <= request.user.profile.level:	
		user = request.user
		my_ques =  get_object_or_404(Question, pk = int(ques_num))
		keys={}
		keys.update(csrf(request))
		keys.update( {'user':request.user, 'my_ques':my_ques } )	
		if request.method == 'POST':
			if int(ques_num) == request.user.profile.level:
				user.profile.tries += 1
				user.profile.save()
				answer=request.POST.get('answer','')
				if my_ques.correct_answer == answer :
					user.profile.score += score_value(request)
					user.profile.level += 1
					user.profile.tries = 0
					user.profile.save()
				return HttpResponseRedirect('/buzz/portal/gordian-knot/ques/'+ str(user.profile.level) + '/')
			else:
				return HttpResponse("Better Luck next time Bro!")
		else:
			return render_to_response('gordian_knot/ques.html',keys)
	else:
		return HttpResponse("Better Luck next time Bro!")
def leaderboard(request):
	user_list = Profile.objects.all().order_by('score')[::-1]
	return render(request, 'gordian_knot/leader.html', {'user_list' : user_list})
