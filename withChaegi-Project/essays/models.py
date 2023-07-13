from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Essay(models.Model):
    essay_title = models.TextField(verbose_name='감상문 제목')
    book_photo = models.ImageField(verbose_name='사진 첨부', null=True, blank=True)
    book_title = models.TextField(verbose_name='책 제목')
    book_author = models.TextField(verbose_name='책 지은이')
    essay_content = models.TextField(verbose_name='상세 내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    view_count = models.IntegerField(verbose_name='조회수', default=0)
    essay_likes = models.IntegerField(verbose_name='좋아요', default=0)
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)

class Comment(models.Model):
    comment_content = models.TextField(verbose_name='내용', max_length=400)
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    essay = models.ForeignKey(to='Essay', on_delete=models.CASCADE)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)