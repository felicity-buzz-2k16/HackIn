from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def index(request):
    return render_to_response('HackIn/index.html')

@login_required
def contest(request):
    return render_to_response('HackIn/contest.html')

@login_required()
def ques1(request):
    print '1'
    if request.method == "GET":
        c = {}
        c.update(csrf(request))
        return render_to_response('HackIn/ques1.html',c)
    else:
        ans = request.POST.get('ans','')
        if ans == "buzz":
            return HttpResponseRedirect('/buzz/portal/HackIn/ques2')
        else:
            c = {}
            c.update(csrf(request))
            return render_to_response('HackIn/ques1.html',c)

@login_required()
def ques2(request):
    print '2'
    if request.method == "GET":
        c = {}
        c.update(csrf(request))
        return render_to_response('HackIn/ques2.html',c)
    else:
        ans = request.POST.get('ans','')
        if ans == "buzz":
            return HttpResponseRedirect('/buzz/portal/HackIn/ques3')
        else:
            c = {}
            c.update(csrf(request))
            return render_to_response('HackIn/ques2.html',c)



@login_required()
def ques3(request):
    print '3'
    if request.method == "GET":
        c = {}
        c.update(csrf(request))
        return render_to_response('HackIn/ques3.html',c)
    else:
        ans = request.POST.get('ans','')
        if ans == "buzz":
            return HttpResponseRedirect('/buzz/portal/HackIn/ques4')
        else:
            c = {}
            c.update(csrf(request))
            return render_to_response('HackIn/ques3.html',c)



@login_required()
def ques4(request):
    print '4'
    if request.method == "GET":
        c = {}
        c.update(csrf(request))
        print 'DDD'
        return render_to_response('HackIn/ques4.html',c)
    else:
        ans = request.POST.get('ans','')
        print '4 - ELSE'
        if ans == "nextlevelunlocked":
            return HttpResponseRedirect('/buzz/portal/HackIn/ques5')
        else:
            c = {}
            c.update(csrf(request))
            return render_to_response('HackIn/ques4.html',c)


@csrf_exempt
@login_required()
def ques5(request):

    if request.method == "GET":
        print 'GETTT'
        context = {}
        context.update(csrf(request))

        # create request context, to pass to template loader
        requestContext = RequestContext(request, context)
        # load template index.html
        templateIndex = loader.get_template('HackIn/ques5.html')
        # get the render-able template
                            
        renderedTemplate = templateIndex.render(requestContext)
        response = HttpResponse()
        # set unsigned cookies
        response.set_cookie('**_buzzNextLevelAccess_**', '0')

        # write render-able template to response
        response.write(renderedTemplate)

        # return response
        return response

        #c = {}
        #c.update(csrf(request))
        #return render_to_response('HackIn/ques5.html',c)
    else:
        CC = request.COOKIES['**_buzzNextLevelAccess_**']
        #print 'COOKIE'
        #print CC
        #print 'COOKIE'
        if int(CC):
            return HttpResponseRedirect('/buzz/portal/HackIn/ques6')
        else:
            c = {}
            c.update(csrf(request))
            return render_to_response('HackIn/ques5.html',c)


def ques6(request):
    if request.method == "GET":

        context = {}
        context.update(csrf(request))

        # create request context, to pass to template loader
        requestContext = RequestContext(request, context)
        # load template index.html
        templateIndex = loader.get_template('HackIn/ques6.html')
        # get the render-able template
                            
        renderedTemplate = templateIndex.render(requestContext)
        response = HttpResponse()
        # set unsigned cookies
        response.set_cookie('**_paerChooSale_**', 0)

        # write render-able template to response
        response.write(renderedTemplate)

        # return response
        return response
    else:
        CC = request.COOKIES['**_paerChooSale_**']

        if int(CC) == 10000:
            return HttpResponseRedirect('/buzz/portal/HackIn/ques7')
        else:
            c = {}
            c.update(csrf(request))
            return render_to_response('HackIn/ques6.html',c)




def ques7(request):
    if request.method == "GET":
        c = {}
        c.update(csrf(request))
        return render_to_response('HackIn/ques7.html',c)
    else:
        ans = request.POST.get('ans','')
        if ans == "lyeskpuaitsaamhak":
            return HttpResponseRedirect('/buzz/portal/HackIn/ques8')
        else:
            c = {}
            c.update(csrf(request))
            return render_to_response('HackIn/ques7.html',c)




def ques8(request):
    if request.method == "GET":
        c = {}
        c.update(csrf(request))
        return render_to_response('HackIn/ques8.html',c)
    else:
        ans = request.POST.get('ans','')
        if ans == "kjaliuKdhJdsab23hjK9231JJJ":
            return HttpResponseRedirect('/buzz/portal/HackIn/ques9')
        else:
            c = {}
            c.update(csrf(request))
            return render_to_response('HackIn/ques8.html',c)



def sendpassword(request):
        return HttpResponse("lkaDDsjdfP0lk")

def ques9(request):
    if request.method == "GET":
        c = {}
        c.update(csrf(request))
        return render_to_response('HackIn/ques9.html',c)
    else:
        ans = request.POST.get('ans','')
        if ans == "lkaDDsjdfP0lk":
            return HttpResponseRedirect('/buzz/portal/HackIn/ques10')
        else:
            c = {}
            c.update(csrf(request))
            return render_to_response('HackIn/ques9.html',c)




def ques10(request):
    if request.method == "GET":
        c = {}
        c.update(csrf(request))
        return render_to_response('HackIn/ques5.html',c)
    else:
        ans = request.POST.get('ans','')
        if ans == "nextlevelunlocked":
            return HttpResponseRedirect('/buzz/portal/HackIn/ques6')
        else:
            c = {}
            c.update(csrf(request))
            return render_to_response('HackIn/ques5.html',c)




def ques11(request):
    if request.method == "GET":
        c = {}
        c.update(csrf(request))
        return render_to_response('HackIn/ques5.html',c)
    else:
        ans = request.POST.get('ans','')
        if ans == "nextlevelunlocked":
            return HttpResponseRedirect('/buzz/portal/HackIn/ques6')
        else:
            c = {}
            c.update(csrf(request))
            return render_to_response('HackIn/ques5.html',c)




def ques12(request):
    if request.method == "GET":
        c = {}
        c.update(csrf(request))
        return render_to_response('HackIn/ques5.html',c)
    else:
        ans = request.POST.get('ans','')
        if ans == "nextlevelunlocked":
            return HttpResponseRedirect('/buzz/portal/HackIn/ques6')
        else:
            c = {}
            c.update(csrf(request))
            return render_to_response('HackIn/ques5.html',c)




def ques13(request):
    if request.method == "GET":
        c = {}
        c.update(csrf(request))
        return render_to_response('HackIn/ques5.html',c)
    else:
        ans = request.POST.get('ans','')
        if ans == "nextlevelunlocked":
            return HttpResponseRedirect('/buzz/portal/HackIn/ques6')
        else:
            c = {}
            c.update(csrf(request))
            return render_to_response('HackIn/ques5.html',c)




def ques14(request):
    if request.method == "GET":
        c = {}
        c.update(csrf(request))
        return render_to_response('HackIn/ques5.html',c)
    else:
        ans = request.POST.get('ans','')
        if ans == "nextlevelunlocked":
            return HttpResponseRedirect('/buzz/portal/HackIn/ques6')
        else:
            c = {}
            c.update(csrf(request))
            return render_to_response('HackIn/ques5.html',c)




def ques15(request):
    if request.method == "GET":
        c = {}
        c.update(csrf(request))
        return render_to_response('HackIn/ques5.html',c)
    else:
        ans = request.POST.get('ans','')
        if ans == "nextlevelunlocked":
            return HttpResponseRedirect('/buzz/portal/HackIn/ques6')
        else:
            c = {}
            c.update(csrf(request))
            return render_to_response('HackIn/ques5.html',c)







