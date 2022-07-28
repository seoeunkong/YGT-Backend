from xml.etree.ElementTree import Comment
from django.shortcuts import render,redirect,get_object_or_404
from .forms import CommentForm, PostForm
from .models import Post, Profile,Comment

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
            unfinished = form.save(commit=False)
            unfinished.author = request.user
            unfinished.save()
            return redirect("home")

    #request method가 GET일 경우
    else:
        form = PostForm()
     #form 입력 html 띄우기
    return render(request,"post_form.html",{"form":form})

def detail(request,post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    return render(request, "detail.html",{"post_detail":post_detail,"comment_form":comment_form})

#댓글 저장
def new_comment(request,post_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.writer = request.user
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.writer_profile = get_object_or_404(Profile, pk=request.user.id)
        finished_form.save()
    return redirect('detail',post_id)