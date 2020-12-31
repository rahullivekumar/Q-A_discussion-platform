from datetime import date, datetime

from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from rest_framework import  viewsets
from .serializers import QuestionSerializer
from .models import Questions, Answers
from django.contrib.auth.models import User, auth


# Create your views here.

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all().order_by('title')
    serializer_class = QuestionSerializer

def home(request):

    data=Questions.objects.all().order_by("-creation_time")
    page=request.GET.get('page',1)
    paginator=Paginator(data,9)
    try:
        data=paginator.page(page)
    except PageNotAnInteger:
        data=paginator.page(1)
    except EmptyPage:
        data=Paginator.page(paginator.num_pages)
    ques={
        "questions_datas": data
    }
    return render(request,'home.html',ques)

def create(request):
    return 1

def signup(request):
    if request.method== "POST":
        print(150)
        email = request.POST['email']
        password1 = request.POST['password1']
        email=email.strip()
        password1=password1.strip()
        if len(email)>0 and len(password1)>0:
            if User.objects.filter(username=email).exists():
                messages.info(request, 'Error: Email already exists')
                return redirect('/signup')
            else:
                user = User.objects.create_user(password=password1,username=email)
                user.save()
                return redirect('/login')
        else:
            messages.info(request, 'Error: Enter Email and Password')
            return redirect('/signup')

    else:
        return render(request,'signup.html')


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user=auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            request.session['userid'] = user.id
            return redirect('/homes')
        else:
            messages.info(request,'Invalid Username/Password')
            return redirect('/login')
    else:
        return render(request,'login.html')

def navv(request):
    return render(request,'navv.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def newques(request):
    if request.method == "POST":
        r=Questions()
        r.title=request.POST['title']
        r.description=request.POST['desc']
        r.count_view=0
        r.tags=request.POST['tags']
        r.creation_time=datetime.now()
        r.user_id=request.session.get('userid')
        r.title=r.title.lstrip()
        r.description=r.description.lstrip()
        if len(r.title)>0 and len(r.description)>0:
            r.save()
            return redirect('home')
        else:
            messages.info(request, 'Enter title and description')
            return redirect('newques')
    else:
        return render(request,'newques.html')

def search(request):
    srh=request.POST['searchbox']
    q=(Questions.objects.filter(title__icontains=srh) | Questions.objects.filter(tags__icontains=srh)).order_by("-creation_time")

    params={'ques':q,
            'ser':srh}
    return render(request,'search.html',params)

def ans(request,qid):
    q=Questions.objects.get(id=qid)
    a=Answers.objects.filter(qid=qid).order_by("-creation_time")
    params = {'ques': q,
              'answers': a,
              }
    return render(request,'ans.html',params)

def delques(request,qid):
    instance=Questions.objects.get(id=qid)
    instance.delete()
    return redirect('home')

def updateques(request,qid):
    q = Questions.objects.get(id=qid)
    if request.method == "POST":
        q.title = request.POST['title'].strip()
        q.tags = request.POST['tags'].strip()
        q.description = request.POST['desc'].strip()
        if len(q.title)>0 and len(q.description)>0:
            q.save()
            return  redirect('home')
        else:
            messages.info(request,"Error: Enter title and description")
            return redirect('editques',qid=qid)
    else:
        return redirect('home')

def viewcount(request,qid):
    q = Questions.objects.get(id=qid)
    q.count_view = q.count_view + 1
    q.save()
    q = Questions.objects.get(id=qid)
    return redirect('ans',qid=qid)



def editques(request,qid):
    q = Questions.objects.get(id=qid)
    return render(request,'editques.html',{'ques':q})

def newans(request,qid):
    if request.method=="POST":
        r=Answers()
        print(request.session.get('userid'))
        r.user_id=request.session.get('userid')
        r.desc=request.POST['desc'].strip()
        r.qid=qid
        r.creation_time=datetime.now()
        if len(r.desc)>0:
            r.save()
            return redirect('ans', qid=qid)
        else:
            messages.info(request,"Error: Enter Answer")
            return redirect('ans', qid=qid)

    return redirect('home')

def delans(request,aid):
    instance = Answers.objects.get(aid=aid)
    qid=instance.qid
    instance.delete()
    return redirect('ans',qid=qid)

def updateans(request,aid):
    a = Answers.objects.get(aid=aid)
    qid = a.qid
    if request.method=="POST":
        a.desc=request.POST['desc'].strip()
        if len(a.desc)>0:
            a.save()
            return redirect('ans', qid=qid)
        else:
            messages.info(request,"Error: Enter answer")
            return  redirect('editans',aid=aid)
    return redirect('ans', qid=qid)

def editans(request,aid):
    a=Answers.objects.get(aid=aid)
    return render(request,'editans.html',{'answer':a})


