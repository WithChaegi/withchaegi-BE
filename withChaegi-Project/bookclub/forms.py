from django.core.exceptions import ValidationError
from django import forms
from .models import BookClub

class BookClubBaseForm(forms.ModelForm):
    class Meta:
        model = BookClub
        fields = "__all__"

class BookClubCreateForm(BookClubBaseForm):
    class Meta(BookClubBaseForm.Meta):
        fields = ['group_name', 'book_photo', 'book_title', 
                  'book_author', 'date1', 'date2', 'date3', 'date4', 'date5', 'time', 'city_location', 
                  'district_location', 'dong_location', 'discussion_field', 
                  'discussion_keywords', 'min_members', 'max_members', 'details']