from django.urls import path
from .views import essay_list_view, essay_create_view, essay_detail_view, essay_update_view, essay_delete_view

app_name = 'essays'

urlpatterns = [
    path('', essay_list_view, name='essay-list'),
    path('new/', essay_create_view),
    path('<int:id>/', essay_detail_view),
    path('<int:id>/edit/', essay_update_view),
    path('<int:id>/delete/', essay_delete_view),
]