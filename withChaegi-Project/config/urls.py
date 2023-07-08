from django.contrib import admin
from django.urls import path, include
from essays.views import index, url_view, url_parameter_view, function_view, class_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('url/', url_view),
    path('url/<str:username>/', url_parameter_view),
    path('fbv/', function_view),
    path('cbv/', class_view.as_view()),

    path('', index, name='index'),
    path('essays/', include('essays.urls', namespace='essays')),

    path('accounts/', include('accounts.urls', namespace='accounts'))
]
