from operator import mod
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

#게시물 모델
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    # #게시글 작성자 학교
    # author_school = models.ForeignKey(UserModel, null =True, blank=True, on_delete=models.CASCADE)
    # #게시글 작성자 학과
    # author_department = models.ForeignKey(UserModel, null =True, blank=True, on_delete=models.CASCADE)
    # #게시글 작성자 학번
    # author_id = models.ForeignKey(UserModel, null =True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, null =True, blank=True, on_delete=models.CASCADE)
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    # #댓글 작성자 학교
    # writer_school = models.ForeignKey(UserModel, null =True, blank=True, on_delete=models.CASCADE)
    # #댓글 작성자 학과
    # writer_department = models.ForeignKey(UserModel, null =True, blank=True, on_delete=models.CASCADE)
    # #댓글 작성자 학번
    # writer_id = models.ForeignKey(UserModel, null =True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment




