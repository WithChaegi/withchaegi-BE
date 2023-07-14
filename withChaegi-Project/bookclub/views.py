from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import BookClub
from .forms import BookClubBaseForm, BookClubCreateForm
from django.db.models import F, Q
import simplejson as json
import datetime
import os
from django.conf import settings

q = Q()

weekday_list = ['월', '화', '수', '목', '금', '토', '일']

def get_weekday(date_string):
    parts = date_string.split('/')
    month = int(parts[0].zfill(2))
    day = int(parts[1])  # 앞에 0을 추가하여 2자리 수로 만듭니다.
    dt = datetime.datetime(2023, month, day)
    weekday = dt.weekday()
    str_weekday = weekday_list[weekday]
    return str_weekday

# 책분야, 인원, 장소, 일시별로 필터링 코드
def filtering(request):
    discussion_field = request.GET.getlist('discussion_field', None)
    max_members = request.GET.get('max_members', None)
    dong_location = request.GET.get('dong_location', None)
    date1 = request.GET.get('date1', None)
    
    # q = Q()

    if discussion_field:
        q &= Q(discussion_field = discussion_field) # 왼(필드명)=오(찾는값) # &=로 필터 추가
    if max_members:
        q &= Q(max_members = max_members)
    if dong_location:
        q &= Q(dong_location = dong_location)
    if date1:
        q &= Q(date1 = date1)
    
    clubs = BookClub.objects.filter(q)
    return clubs

def main_page(request):
    bookclub_entirelist = BookClub.objects.all()[:4]
    bookclub_popularlist = BookClub.objects.all().order_by('-likes')[:4]
    context = {
        'bookclub_entirelist' : bookclub_entirelist,
        'bookclub_popularlist' : bookclub_popularlist,
    }
    return render(request, 'club/offline-main.html', context)

def catetory_filtering(q):
    # q에 해당하는 값을 필터링하여 적절한 결과를 반환하는 로직을 작성하세요.
    if q == '1':
        clubs = BookClub.objects.filter(small_category='소설/시')
    elif q == '2':
        clubs = BookClub.objects.filter(small_category='인문')
    elif q == '3':
        clubs = BookClub.objects.filter(small_category='사회')
    elif q == '4':
        clubs = BookClub.objects.filter(small_category='역사')
    elif q == '5':
        clubs = BookClub.objects.filter(small_category='예술')
    elif q == '6':
        clubs = BookClub.objects.filter(small_category='과학')
    elif q == '7':
        clubs = BookClub.objects.filter(small_category='경제 경영')
    else:
        clubs = BookClub.objects.all()  # 선택하지 않았을 경우 빈 결과 반환

    return clubs

def get_weekday_four_str(date_string):
    parts = date_string.split('-')

    dt = datetime.datetime(int(parts[0]), int(parts[1]), int(parts[2]))
    weekday = dt.weekday() # (0은 월요일, 6은 일요일)
    str_weekday = weekday_list[weekday]
    return str_weekday

# 전체 독서 모임 확인
def entire_list(request):
    if request.method == 'GET':
        selected_book = request.GET.get('bookBtn')
        if selected_book: # 필터링이 걸려있다면
            clubs = BookClub.objects.filter(small_category=selected_book)
        else:
            clubs = BookClub.objects.all()

        club_list = []
        temp_club_data = []  # 4개씩 묶은 임시 리스트

        for index, club in enumerate(clubs):
            club_data = {
                'club_id': club.id,
                'group_name': club.group_name,
                'book_photo': club.book_photo,
                'book_title': club.book_title,
                'district_location': club.district_location,
                'dong_location': club.dong_location,
                'date1': club.date1,
                'time': club.time,
                'small_category': club.small_category,
                'weekday1': get_weekday(club.date1) if len(club.date1) <= 4 else get_weekday_four_str(club.date1)
            }
            temp_club_data.append(club_data)

            # 임시 리스트 초기화
            if (index + 1) % 4 == 0 or (index + 1) == len(clubs):
                club_list.append(temp_club_data)
                temp_club_data = []

        context = {'clubs': club_list, 'clubs_list_count': len(clubs)}
        # return render(request, 'club/entire_list.html', context)
        return render(request, 'club/main-club.html', context)

# 인기 독서 모임 확인
def popular_list(request):
    if request.method == 'GET':
        selected_book = request.GET.get('bookBtn')
        if selected_book: # 필터링이 걸려있다면
            clubs = BookClub.objects.filter(small_category=selected_book)
        else:
            clubs = BookClub.objects.all().order_by('-likes')

        club_list = []
        temp_club_data = []  # 4개씩 묶은 임시 리스트

        for index, club in enumerate(clubs):
            club_data = {
                'club_id': club.id,
                'group_name': club.group_name,
                'book_photo': club.book_photo,
                'book_title': club.book_title,
                'district_location': club.district_location,
                'dong_location': club.dong_location,
                'date1': club.date1,
                'time': club.time,
                'small_category': club.small_category,
                'weekday1': get_weekday(club.date1) if len(club.date1) <= 4 else get_weekday_four_str(club.date1)
            }
            temp_club_data.append(club_data)

            # 임시 리스트 초기화
            if (index + 1) % 4 == 0 or (index + 1) == len(clubs):
                club_list.append(temp_club_data)
                temp_club_data = []

        context = {'clubs': club_list, 'clubs_list_count': len(clubs)}
        # return render(request, 'club/entire_list.html', context)
        return render(request, 'club/main-club.html', context)

# 특정 독서 모임 확인
def club_detail(request, pk):
    if request.method == 'GET':
        club = get_object_or_404(BookClub, id=pk)

        weekday1 = None
        weekday2 = None
        weekday3 = None
        weekday4 = None
        weekday5 = None

        if club.date1:
            weekday1 = get_weekday(club.date1)
        if club.date2:
            weekday2 = get_weekday(club.date2)
        if club.date3:
            weekday3 = get_weekday(club.date3)
        if club.date4:
            weekday4 = get_weekday(club.date4)
        if club.date5:
            weekday5 = get_weekday(club.date5)

        club_data = {
            'club_id': club.id,
            'group_name': club.group_name,
            'book_photo': club.book_photo,
            'book_title': club.book_title,
            'book_author': club.book_author,
            'regularity': club.regularity,
            'date1': club.date1,
            'date2': club.date2,
            'date3': club.date3,
            'date4': club.date4,
            'date5': club.date5,
            'time': club.time,
            'district_location': club.district_location,
            'dong_location': club.dong_location,
            'full_address': club.full_address,
            'discussion_field': club.discussion_field,
            'discussion_keywords': club.discussion_keywords,
            'min_members': club.min_members,
            'max_members': club.max_members,
            'applied_members': club.applied_members,
            'club_details': club.details,
            'likes': club.likes,
            'remaining': club.max_members - club.applied_members,
            'weekday1': weekday1 if weekday1 is not None else None,
            'weekday2': weekday2 if weekday2 is not None else None,
            'weekday3': weekday3 if weekday3 is not None else None,
            'weekday4': weekday4 if weekday4 is not None else None,
            'weekday5': weekday5 if weekday5 is not None else None,
        }

        context = {'club': club_data}
        # return render(request, 'club/club_detail.html', context)
        return render(request, 'club/main-detail.html', context)

# 독서모임 생성
def create_club(request):
    if request.method == 'POST':
        # form = BookClubBaseForm(request.POST, request.FILES)
        group_name = request.POST.get('club_title')
        book_photo = ''
        book_title = request.POST.get('book_title')
        book_author = request.POST.get('book_author')
        regularity = request.POST.get('club_round')
        date1 = request.POST.get('club_date')
        time = request.POST.get('club_time')
        city_location = request.POST.get('club_location')
        district_location = request.POST.get('club_district')
        dong_location = request.POST.get('club_town')
        discussion_field = request.POST.get('discuss')
        discussion_keywords = request.POST.get('club_keywords')
        min_members = request.POST.get('min_members')
        max_members = request.POST.get('max_members')
        details = request.POST.get('club_details')

        parts = date1.split('-')

        new_date = f"{int(parts[1])}/{int(parts[2])}"

        dt = datetime.datetime(int(parts[0]), int(parts[1]), int(parts[2]))
        weekday = dt.weekday() # (0은 월요일, 6은 일요일)

        weekday_list = ['월', '화', '수', '목', '금', '토', '일']
        for i in range(7):
            if weekday == i:
                str_weekday = weekday_list[i]
                break

        book_club = BookClub.objects.create(
            group_name = group_name,
            book_photo = book_photo,
            book_title = book_title,
            book_author = book_author,
            regularity = regularity,
            date1 = new_date,
            time = time,
            city_location = city_location,
            district_location = district_location,
            dong_location = dong_location,
            full_address = city_location + ' ' + district_location + ' ' + dong_location,
            discussion_field = discussion_field,
            discussion_keywords = discussion_keywords,
            min_members = min_members,
            max_members = max_members,
            details = details,
            weekday1 = str_weekday
        )


        # context = {'club_id': BookClub.id}
        # return render(request, 'club/entire_list.html', context)
        # 생성된 독서클럽 detail로 이동
        return redirect('/club/' + str(book_club.id))
    # return HttpResponse("Invalid form data or request method.")
    return render(request, 'club/book_apply.html')

# 독서 모임 신청
def apply_club(request, pk): # , user_id
    if request.method == 'GET':
        club = get_object_or_404(BookClub, id=pk)

        # 최대 멤버 수 초과하는지 확인
        if club.applied_members < club.max_members:
            # applied_members = request.POST.get('applied_members')
            # 신청 멤버 수 update
            # club = BookClub.objects.update(
            #     # applied_members=applied_members+1
            #     applied_members = F('applied_members') + 1 # DB 내에서 바로 업데이트하도록
            # )
            # club.applied_members += 1
            club.applied_members = F('applied_members') + 1
            club.save()

            context = {'club_id': club.id}
            # return render(request, 'club/entire_list.html', context)
            # return render(request, 'club/main-detail.html', context)
            return redirect('/club/' + str(pk))

    # return render(request, 'club/club_detail.html')
    # return render(request, 'club/main-detail.html')
    return redirect('/club/' + str(pk))