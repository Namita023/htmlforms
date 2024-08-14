from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.

def insert_topics(request):
    if request.method=="POST":
        topics=request.POST['topicname']
        TO=Topic.objects.get_or_create(topic_name=topics)[0]
        TO.save()
        return HttpResponse('Topic is created')
    return render(request,"insert_topics.html")

def htmlform(request):
    if request.method=="POST":
        #return HttpResponse(request.POST)
        return HttpResponse(request.POST['username'])
    return render(request,"htmlform.html")

def insert_webpages(request):
    LTO=Topic.objects.all()
    d={"LTO":LTO}
    if request.method=="POST":
        tname=request.POST['topicname']
        name=request.POST['name']
        url=request.POST['url']
        email=request.POST['email']
        TO=Topic.objects.get(topic_name=tname)
        WPO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)[0]
        WPO.save()
        return HttpResponse('Webpage is created')
    return render(request,'insert_webpages.html',d)

def insert_accessrecords(request):
    LWO=Webpage.objects.all()
    d={'WP':LWO}
    if request.method=='POST':
        n=request.POST['name']
        NO=Webpage.objects.get(id=n)
        a=request.POST['author']
        d=request.POST['date']
        ARO=AccessRecord.objects.get_or_create(name=NO,author=a,date=d)[0]
        ARO.save()
        return HttpResponse('Access Record is created. ')
    return render(request,'insert_accessrecords.html',d)

def select_topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=="POST":
        topics=request.POST.getlist('topic')
        webpages=Webpage.objects.none()
        for tn in topics:
            webpages=webpages|Webpage.objects.filter(topic_name=tn)
        d1={'webpages':webpages}
        return render(request,'display_webpages.html',d1)
    return render(request,'select_topic.html',d)

def checkbox(request):
    d={"LTO":Topic.objects.all()}
    return render(request,"checkbox.html",d)

