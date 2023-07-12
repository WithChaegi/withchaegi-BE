from django.urls import path
from .views import essay_list_view, essay_main_view, essay_entirelist_view, essay_popularlist_view, essay_create_view, essay_detail_view, essay_update_view, essay_delete_view

app_name = 'essays'

urlpatterns = [
    # path('', essay_main_view, name='essay-list'),
    path('', essay_main_view, name='essay-main'),
    path('main', essay_main_view, name='essay-main'),
    path('entirelist', essay_entirelist_view, name='essay-entirelist'),
    path('popularlist', essay_popularlist_view, name='essay-popularlist'),
    path('create/', essay_create_view, name='essay-create'),
    path('<int:id>/', essay_detail_view, name='essay-detail'),
    path('<int:id>/edit/', essay_update_view),
    path('<int:id>/delete/', essay_delete_view),
]