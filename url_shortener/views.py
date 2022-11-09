from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import LongtoShort
#when the following is called it responses with an string using the httpResponsemodule
def hw(req):
    return HttpResponse("hello")

#request contains all the information about the activity happen on the URL
#post,get as per the action on the particular endpoint
#req.post provide the detail entered on the form with an particular csrftoken
def home_page(req):
    context={'submitted':False}
    if req.method=="POST":
        data=req.POST
        longurl=data['longurl']
        #the url on which the page is rendered is the build_absolute_uri()
        customurl=req.build_absolute_uri()+ data['custom_name']
        context['long_url']=longurl
        context['short_url']=customurl
        context['submitted']=True
        obj=LongtoShort(long_url=longurl,custom_name=customurl)
        obj.save()
    else:
        print("haven't submit the form")
    #render(request,file_to_render,data_from_model)
    #the render method searches for the html page in the templates folder automatically
    return render(req,"index.html",context)