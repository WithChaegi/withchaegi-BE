from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import BookClub
from .forms import BookClubBaseForm, BookClubCreateForm
from django.db.models import F, Q
import simplejson as json

q = Q()

# 책분야, 인원, 장소, 일시별로 필터링 코드
def filtering(request):
    discussion_field = request.GET.getlist('discussion_field', None)
    max_members = request.GET.get('max_members', None)
    dong_location = request.GET.get('dong_location', None)
    date = request.GET.get('date', None)
    
    # q = Q()

    if discussion_field:
        q &= Q(discussion_field = discussion_field) # 왼(필드명)=오(찾는값) # &=로 필터 추가
    if max_members:
        q &= Q(max_members = max_members)
    if dong_location:
        q &= Q(dong_location = dong_location)
    if date:
        q &= Q(date = date)
    
    clubs = BookClub.objects.filter(q)
    return clubs

# 전체 독서 모임 확인
def entire_list(request):
    if request.method == 'GET':
        if q: # 필터링이 걸려있다면
            clubs = filtering(request)
        else:
            clubs = BookClub.objects.all()

        club_list = []
        for club in clubs:
            club_data = {
                'club_id': club.id,
                'group_name': club.group_name,
                'book_photo': club.book_photo,
                'book_title': club.book_title,
                'district_location': club.district_location,
                'date': club.date[0], # 첫번째 모임 날짜
                'time': club.time
            }
            club_list.append(club_data)

        context = {'clubs': club_list}
        return render(request, 'club/entire_list.html', context)

# 인기 독서 모임 확인
def popular_list(request):
    if request.method == 'GET':
        if q: # 필터링이 걸려있다면
            clubs = filtering(request)
        else:
            clubs = BookClub.objects.order_by('-likes') # likes 많은 순으로 정렬(내림차순)

        club_list = []
        for club in clubs:
            club_data = {
                'club_id': club.id,
                'group_name': club.group_name,
                'book_photo': club.book_photo,
                'book_title': club.book_title,
                'district_location': club.district_location,
                'date': club.date[0], # 첫번째 모임 날짜
                'time': club.time
                # 'likes': club.likes
            }
            club_list.append(club_data)

        context = {'clubs': club_list}
        return render(request, 'club/popular_list.html', context)

# 특정 독서 모임 확인
def club_detail(request, pk):
    if request.method == 'GET':
        club = get_object_or_404(BookClub, id=pk)

        club_data = {
            'group_name': club.group_name,
            'book_photo': club.book_photo,
            'book_title': club.book_title,
            'book_author': club.book_author,
            'regularity': club.regularity,
            'date': club.date,
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
            'likes': club.likes
        }

        context = {'club': club_data}
        return render(request, 'club/club_detail.html', context)

# 독서모임 생성
def create_club(request):
    if request.method == 'POST':
        form = BookClubBaseForm(request.POST, request.FILES)

        if form.is_valid():
            date_values = form.cleaned_data['date']
            # date_strings = [date.strftime('%Y-%m-%d') for date in date_values]
            date_strings = [date for date in date_values]
            time_values = form.cleaned_data['time']
            # time_strings = [time.strftime('%H:%M:%S') for time in time_values]
            time_strings = [time for time in time_values]
            book_club = BookClub.objects.create(
                group_name = form.cleaned_data['group_name'],
                book_photo = form.cleaned_data['book_photo'],
                book_title = form.cleaned_data['book_title'],
                book_author = form.cleaned_data['book_author'],
                regularity = form.cleaned_data['regularity'],
                # date = form.cleaned_data['date'],
                # date = date_strings,
                # time = form.cleaned_data['time'],
                # time = time_strings,
                city_location = form.cleaned_data['city_location'],
                district_location = form.cleaned_data['district_location'],
                dong_location = form.cleaned_data['dong_location'],
                discussion_field = form.cleaned_data['discussion_field'],
                discussion_keywords = form.cleaned_data['discussion_keywords'],
                min_members = form.cleaned_data['min_members'],
                max_members = form.cleaned_data['max_members'],
                details = form.cleaned_data['details']
            )

            # for date_string, time_string in zip(date_strings, time_strings):
            #     book_club.date.append(date_string)
            #     book_club.time.append(time_string)
            # book_club.date = date_strings
            # book_club.time = time_strings
            book_club.date = json.dumps(date_strings)
            book_club.time = json.dumps(time_strings)

            book_club.save()

            context = {'club_id': BookClub.id}
            return render(request, 'club/entire_list.html', context)
    else:
        form = BookClubBaseForm()
    # return HttpResponse("Invalid form data or request method.")
    return render(request, 'club/create.html', {'form': form})

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
            return render(request, 'club/entire_list.html', context)
            # return redirect('/club/entire_list')

    return render(request, 'club/club_detail.html')
    # return redirect('/club/entire_list')