from django.contrib import admin
from django.urls import path
from postapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #게시글 목록 
    path('', views.home, name='home'),

    #게시글 작성
    path('postcreate', views.postcreate, name='postcreate'),

    #세부 페이지
    path('detail/<int:post_id>', views.detail, name='detail'),
]
