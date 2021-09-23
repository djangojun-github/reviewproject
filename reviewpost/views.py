from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from .models import ReviewModel
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.

def signupview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        try:
            User.objects.create_user(username_data, '', password_data)
        except IntegrityError:
            return render(request, 'signup.html', {'error':'このユーザは既に登録されています。'})
    else:
        return render(request, 'signup.html', {})
    return render(request, 'signup.html', {})

def loginview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        user = authenticate(request, username=username_data, password=password_data)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect('list')
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html', {'error':'UsernameかPasswordに誤りがあります。'})
    else:
        print(User.objects.all())
        return render(request, 'login.html')

@login_required
def listview(request):
    object_list = ReviewModel.objects.all()
    return render(request, 'list.html', { 'object_list':object_list })

@login_required
def detailview(request, pk):
    object = ReviewModel.objects.get(pk=pk)
    print('詳細画面にログインしているユーザ：' + request.user.get_username() + str(request.user.id))
    return render(request, 'detail.html', { 'object':object })

class CreateClass(CreateView):
    template_name = 'create.html'
    model = ReviewModel
    fields = ('title', 'content', 'author', 'images', 'evaluation')
    success_url = reverse_lazy('list')

def evaluationview(request, pk):
    post = ReviewModel.objects.get(pk=pk)
    author_name = request.user.get_username() + str(request.user.id)
    if author_name in post.useful_review_record.split(" "):
        return redirect('list')
    else:
        post.useful_review = post.useful_review + 1
        if post.useful_review > 1:
            post.useful_review_record = post.useful_review_record + " "
        post.useful_review_record = post.useful_review_record + author_name
        post.save()
        return redirect('list')
