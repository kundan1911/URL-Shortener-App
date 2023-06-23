from django.shortcuts import render,redirect
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
    context={'submitted':False,'repeatAlias':False}
    if req.method=="POST":
        data=req.POST
        longurl=data['longurl']
        #the url on which the page is rendered is the build_absolute_uri()
        # customurl=req.build_absolute_uri()+ data['custom_name']
        customurl=data['custom_name']
        try:
            context['long_url']=longurl
            context['short_url']=req.build_absolute_uri() + customurl
          
            
            obj=LongtoShort(long_url=longurl,custom_name=customurl)
            obj.save()
            context['submitted']=True
            context['clickCount']=obj.clicks
            context['date']=obj.date
        except:
            context={"repeatAlias":True}
           
    else:
        print("haven't submit the form")
    #render(request,file_to_render,data_from_model)
    #the render method searches for the html page in the templates folder automatically
    return render(req,"index.html",context)



def allAnalyticsPage(req):
    allEntry=LongtoShort.objects.all();
    return render(req,'all-analytics.html',{"entries":allEntry})

def redirect_view(req,dynamicEndPnt):
    print(dynamicEndPnt);
    currentShrtTolong=LongtoShort.objects.filter(custom_name=dynamicEndPnt);
   
    if len(currentShrtTolong)==0:
        return HttpResponse("shorturl does not exist")
    else:
        entry=currentShrtTolong[0];
        entry.clicks=entry.clicks+1;
        entry.save();
        print(entry.long_url);

        return redirect(entry.long_url)