from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required

from .models import Essay
from .models import Comment

def main(request):
    essay_popularlist = Essay.objects.all().order_by('-created_at')[:3] # 최신순 정렬
    # essay_list = Essay.objects.all().order_by('-essay_likes') # 인기순 정렬
    context = {
        'essay_popularlist' : essay_popularlist
    }
    return render(request, 'main.html', context)

def essay_list_view(request):
    # essay_list = Essay.objects.all() # Essay 전체 데이터 조회
    essay_list = Essay.objects.all().order_by('-created_at') # 최신순 정렬
    # essay_list = Essay.objects.all().order_by('-essay_likes') # 인기순 정렬
    context = {
        'essay_list' : essay_list
    }
    return render(request, 'essays/essay_list.html', context)

def essay_main_view(request):
    # essay_list = Essay.objects.all() # Essay 전체 데이터 조회
    essay_entirelist = Essay.objects.all().order_by('-created_at')[:3] # 최신순 정렬
    essay_popularlist1 = Essay.objects.all().order_by('-created_at')[:1]
    essay_popularlist2 = Essay.objects.all().order_by('-created_at')[1:2]
    essay_popularlist3 = Essay.objects.all().order_by('-created_at')[2:3]
    # essay_popularlist = Essay.objects.all().order_by('-essay_likes') # 인기순 정렬
    context = {
        'essay_entirelist' : essay_entirelist,
        'essay_popularlist1' : essay_popularlist1,
        'essay_popularlist2' : essay_popularlist2,
        'essay_popularlist3' : essay_popularlist3
    }
    return render(request, 'essays/essay_main.html', context)

def essay_entirelist_view(request):
    essay_entirelist = Essay.objects.all().order_by('-created_at') # 최신순 정렬
    # essay_list = Essay.objects.all().order_by('-essay_likes') # 인기순 정렬
    context = {
        'essay_entirelist' : essay_entirelist
    }
    return render(request, 'essays/essay_entirelist.html', context)

def essay_popularlist_view(request):
    # essay_popularlist = Essay.objects.all().order_by('-created_at') # 최신순 정렬
    essay_popularlist = Essay.objects.all().order_by('-essay_likes') # 인기순 정렬
    context = {
        'essay_popularlist' : essay_popularlist
    }
    return render(request, 'essays/essay_popularlist.html', context)

def essay_detail_view(request, id):
    try:
        essay = Essay.objects.get(id=id)
    except Essay.DoesNotExist:
        return redirect('main')
    # comment_list = Comment.objects.all().order_by('-created_at') # 최신순 정렬
    # comment = Comment.objects.all().get(essay=id)
    context = {
        'essay' : essay,
        # 'comment' : comment
    }
    return render(request, 'essays/essay_detail.html', context)

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
        return redirect('main')

def essay_update_view(request, id): # 수정 기능인데 사용X
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