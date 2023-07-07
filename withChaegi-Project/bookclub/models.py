from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class BookClub(models.Model):
    group_name = models.CharField(verbose_name='모임명', max_length=30)
    book_photo = models.CharField(verbose_name='사진', max_length=128)
    book_title = models.CharField(verbose_name='책 제목', max_length=30)
    book_author = models.CharField(verbose_name='지은이', max_length=10)
    regularity = models.BooleanField(verbose_name='정기/비정기', default=False) # True(정기)/False(비정기)
    date = ArrayField(models.CharField(verbose_name='날짜', max_length=20), default=list)
    time = ArrayField(models.CharField(verbose_name='시간', max_length=20), default=list)
    city_location = models.CharField(verbose_name='장소(시/도)', max_length=10)
    district_location = models.CharField(verbose_name='장소(구/시/군)', max_length=10)
    dong_location = models.CharField(verbose_name='장소(동/읍/면)', max_length=10)
    full_address = models.CharField(verbose_name='전체 주소', max_length=50)
    discussion_field = models.CharField(verbose_name='토론 분야', max_length=10)
    discussion_keywords = models.CharField(verbose_name='토론 키워드', max_length=10)
    min_members = models.IntegerField(verbose_name='최소 멤버수', default=1, validators=[MinValueValidator(1)])
    max_members = models.IntegerField(verbose_name='최대 멤버수', default=6, validators=[MaxValueValidator(20)])
    applied_members = models.IntegerField(verbose_name='신청한 멤버수', default=0)
    details = models.CharField(verbose_name='클럽 상세 내용', max_length=400, blank=True)
    likes = models.IntegerField(verbose_name='좋아요 수', default=0)

    def validate_member_num(num):
        pass # 아직 작성X # applied_members가 max_members보다 큰지 판별하기 위해 사용할 예정