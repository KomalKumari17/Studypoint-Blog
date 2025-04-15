from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def homePage(req):
    data = {}
    data['title'] = "Recent Topics"
    data['categories'] = Topics.objects.all()
    data['posts'] = Content.objects.all()
    data['tutorials'] = Tutorial.objects.all()
    return render(req, "home.html", data)

def filter(req, topic_id):
    data = {}
    topic = Topics.objects.get(pk=topic_id)
    data['title'] = f"{topic.name}"
    data['categories'] = Topics.objects.all()
    data['tutorials'] = Tutorial.objects.filter(topic__id=topic_id)
    data['active_category_id'] = topic_id
    return render(req, 'home.html', data)

def search(req):
    query = req.GET.get('q', '')  
    data = {}

    if query:
        data['title'] = f"Search Results for '{query}'"
        data['categories'] = Topics.objects.all()
        data['tutorials'] = Tutorial.objects.filter(Q(name__icontains=query))
        data['posts'] = Content.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    else:
        data['title'] = "Search Results"
        data['categories'] = Topics.objects.all()
        data['tutorials'] = Tutorial.objects.all()
        data['posts'] = Content.objects.all()

    return render(req, 'home.html', data)

def view(req, tutorial_id):
    tutorial = Tutorial.objects.get(pk=tutorial_id)
    data={}
    data['title'] = tutorial.name
    data['categories'] = Topics.objects.all()
    data['tutorial'] = tutorial
    data['posts'] = Content.objects.filter(tutorial_id=tutorial_id)
    return render(req, 'viewPage.html', data)


def singleView(req, content_id):
    content = Content.objects.get(pk=content_id)
    data={}
    data['title'] = content.title
    data['categories'] = Topics.objects.all()
    data['post'] = Content.objects.get(id=content_id)
    data['comments'] = Comment.objects.filter(content_id=content_id)
    return render(req, 'singleView.html', data)


def saveComment(req, content_id):
    comment_text = req.POST.get('comment')
    content = Content.objects.get(pk=content_id)
    comment = Comment(content_id=content, user_id=req.user, comment=comment_text)
    comment.save()
    return redirect(singleView, content_id=content_id)

def loginView(req):
    form = AuthenticationForm(req, data=req.POST)
    data={}
    if req.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(req, user)
                return redirect('homePage')

    data['form'] = form
    return render(req, "login.html", data)

def register(req):
    form = UserCreationForm(req.POST or None)
    if req.method == 'POST':
        if form.is_valid():
            userform = form.save(commit=False)
            userform.is_staff = True
            userform.is_superuser = True
            userform.save()
            return redirect('login')
    data={}
    data['form'] = form
    return render(req, "register.html", data)

def logoutFilter(req):
    logout(req)
    return redirect("login")

