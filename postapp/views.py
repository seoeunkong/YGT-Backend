from django.shortcuts import render
from .forms import PostForm

def home(request):
    return render(request,'index.html')

def postcreate(request):
    #request method가 POST일 경우
    if request.method == "POST":
         #입력값 저장
        pass

    #request method가 GET일 경우
    else:
        form = PostForm()
     #form 입력 html 띄우기
    return render(request,"post_form.html",{"form":form})