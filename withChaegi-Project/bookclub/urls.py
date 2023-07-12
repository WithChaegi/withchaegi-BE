from django.urls import path

from .views import main_page, entire_list, popular_list, club_detail, create_club, apply_club

app_name = 'bookclub'

urlpatterns = [
    path('main', main_page, name='main_page'),
    path('entirelist', entire_list, name='entirelist'),
    path('popularlist', popular_list, name='popularlist'),
    path('<int:pk>', club_detail, name='club_detail'),
    path('create', create_club, name='create_club'),
    path('<int:pk>/apply', apply_club, name='apply_club'),
    # path('<int:pk>/apply/<int:pk>', apply_club, name='apply_club'),
]