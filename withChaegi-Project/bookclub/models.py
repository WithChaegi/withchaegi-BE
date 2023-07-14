from django.db import models
# from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator
import os
# from django.utils.deconstruct import deconstructible

# @deconstructible
# class BookClubPhotoPath(object, id):
#     def __call__(self, instance, filename):
#         return f"bookclub/{id}.jfif"

# Create your models here.
class BookClub(models.Model):
    group_name = models.CharField(verbose_name='모임명', max_length=30)
    book_photo = models.ImageField(verbose_name='사진', upload_to='bookclub/', default='bookclub/dallergut.jfif', blank=True) # '/media/'+'bookclub/' # default='default_photo.png'
    book_title = models.CharField(verbose_name='책 제목', max_length=30)
    book_author = models.CharField(verbose_name='지은이', max_length=10)
    regularity = models.BooleanField(verbose_name='정기/비정기', default=False) # True(정기)/False(비정기)
    date1 = models.CharField(verbose_name='1회 날짜', max_length=20, blank=True)
    date2 = models.CharField(verbose_name='2회 날짜', max_length=20, blank=True)
    date3 = models.CharField(verbose_name='3회 날짜', max_length=20, blank=True)
    date4 = models.CharField(verbose_name='4회 날짜', max_length=20, blank=True)
    date5 = models.CharField(verbose_name='5회 날짜', max_length=20, blank=True)
    weekday1 = models.CharField(verbose_name='1회 요일', max_length=3, blank=True)
    weekday2 = models.CharField(verbose_name='2회 요일', max_length=3, blank=True)
    weekday3 = models.CharField(verbose_name='3회 요일', max_length=3, blank=True)
    weekday4 = models.CharField(verbose_name='4회 요일', max_length=3, blank=True)
    weekday5 = models.CharField(verbose_name='5회 요일', max_length=3, blank=True)
    time = models.CharField(verbose_name='시간', max_length=20)
    city_location = models.CharField(verbose_name='장소(시/도)', max_length=10)
    district_location = models.CharField(verbose_name='장소(구/시/군)', max_length=10)
    dong_location = models.CharField(verbose_name='장소(동/읍/면)', max_length=10)
    full_address = models.CharField(verbose_name='전체 주소', max_length=50)
    discussion_field = models.CharField(verbose_name='토론 분야', max_length=10)
    discussion_keywords = models.CharField(verbose_name='토론 키워드', max_length=10)
    min_members = models.IntegerField(verbose_name='최소 멤버수', default=3, validators=[MinValueValidator(1)])
    max_members = models.IntegerField(verbose_name='최대 멤버수', default=6, validators=[MaxValueValidator(20)])
    applied_members = models.IntegerField(verbose_name='신청한 멤버수', default=0)
    details = models.CharField(verbose_name='클럽 상세 내용', max_length=400, blank=True)
    likes = models.IntegerField(verbose_name='좋아요 수', default=0)
    big_category=models.CharField(verbose_name='카테고리1', max_length=10, blank=True)
    middle_category=models.CharField(verbose_name='카테고리2', max_length=10, blank=True)
    small_category=models.CharField(verbose_name='카테고리3', max_length=10, blank=True)

    # # book_photo 파일명 id값으로 변경
    # def save(self, *args, **kwargs):
    #     if self.id and self.book_photo:
    #         old_file_path = self.book_photo.path
    #         filename = f"{self.id}.jfif"
    #         self.book_photo.name = filename
    #         # new_file_path = os.path.join(os.path.dirname(old_file_path), filename)
    #         new_file_path = os.path.join('/media/bookclub/', filename)
    #         os.rename(old_file_path, new_file_path)
    #         self.save(update_fields=['book_photo'])

    #     super().save(*args, **kwargs)