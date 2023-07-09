from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required

from .models import Essay

def index(request):
    return render(request, 'index.html')

def essay_list_view(request):
    return render(request, 'essays/essay_list.html')

def essay_detail_view(request, id):
    return render(request, 'essays/essay_detail.html')

@login_required
def essay_create_view(request):
    if request.method == 'GET':
        return render(request, 'essays/essay_form.html')
    else:
        essay_title = request.POST.get('essay_title')
        book_photo = request.FILES.get('image')
        book_title = request.POST.get('bookTitle')
        book_author = request.POST.get('bookAuthor')
        essay_content = request.POST.get('content')
        print(essay_title)
        print(book_photo)
        
        Essay.objects.create(
            essay_title=essay_title,
            book_photo=book_photo,
            book_title=book_title,
            book_author=book_author,
            essay_content=essay_content,
            writer=request.user
        )
        return redirect('index')

def essay_update_view(request, id):
    return render(request, 'essays/essay_form.html')

def essay_delete_view(request, id):
    return render(request, 'essays/essay_confirm_delete.html')




def url_view(request):
    return HttpResponse('url_view')

def url_parameter_view(request, username):
    print('url_parameter_view()')
    print(username)
    print(f'username: {username}')
    print(f'request.GET: {request.GET}')
    return HttpResponse(username)

def function_view(request):
    print(f'request.method: {request.method}')
    if request.method == 'GET':
        print(f'request.GET: {request.GET}')
    elif request.method == 'POST':
        print(f'request.POST: {request.POST}')
    return render(request, 'view.html')

class class_view(ListView):
    model = Essay
    template_name = 'cbv_view.html'