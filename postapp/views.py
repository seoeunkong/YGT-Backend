import profile
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
            unfinished.author_profile = get_object_or_404(Profile, pk=request.user.id)
            unfinished.save()
            return redirect("home")

    #request method가 GET일 경우
    else:
        form = PostForm()
     #form 입력 html 띄우기
    return render(request,"post_form.html",{"form":form})

def detail(request,post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    profile_detail = get_object_or_404(Profile, pk=request.user.id)
    comment_form = CommentForm()
    return render(request, "detail.html",{"post_detail":post_detail,"comment_form":comment_form,"profile":profile_detail})

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

#좋아요 게시글
def post_like(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.like_post.filter(id=post_id).exists():
        profile.like_post.remove(post)
        post.like_count -= 1
        post.save()
    else:
        profile.like_post.add(post)
        post.like_count += 1

        post.save()
    return redirect("detail",post_id)

#좋아요 게시글
# def comment_like(request,comment_id):
#     comment = get_object_or_404(Comment, pk=comment_id)
#     user = request.user
#     profile = Profile.objects.get(user=user)
#     if profile.like_comment.filter(id=comment_id).exists():
#         profile.like_comment.remove(comment)
#         comment.like_count -= 1
#         comment.save()
#     else:
#         profile.like_comment.add(comment)
#         comment.like_count += 1

#         comment.save()
#     return redirect("detail",comment_id)

def comment_like(request,post_id):
    comment = Comment.objects.get(post=post_id)
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.like_comment.filter(id=comment.id).exists():
        profile.like_comment.remove(comment)
        comment.like_count -= 1
        comment.save()
    else:
        profile.like_comment.add(comment)
        comment.like_count += 1

        comment.save()
    return redirect("detail",post_id)


