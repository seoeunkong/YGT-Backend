from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Post

def home(request):
    #posts = Post.objects.all()
    posts = Post.objects.filter().order_by("-date")
    return render(request,'index.html',{"posts":posts})

def postcreate(request):
    #request method가 POST일 경우
    if request.method == "POST" or request.method == "FILES":
         #입력값 저장
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")

    #request method가 GET일 경우
    else:
        form = PostForm()
     #form 입력 html 띄우기
    return render(request,"post_form.html",{"form":form})