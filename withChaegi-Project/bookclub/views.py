from django.shortcuts import render, get_object_or_404
from .models import BookClub

# 전체 독서 모임 확인
def entire_list(request):
    if request.method == 'GET':
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
def club_detail(request, club_id):
    if request.method == 'GET':
        club = get_object_or_404(BookClub, id=club_id)

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
        group_name = request.POST.get('group_name')
        book_photo = request.POST.get('book_photo')
        book_title = request.POST.get('book_title')
        book_author = request.POST.get('book_author')
        date = request.POST.get('date')
        time = request.POST.get('time')
        city_location = request.POST.get('city_location')
        district_location = request.POST.get('district_location')
        dong_location = request.POST.get('dong_location')
        discussion_field = request.POST.get('discussion_field')
        discussion_keywords = request.POST.get('discussion_keywords')
        min_members = request.POST.get('min_members')
        max_members = request.POST.get('max_members')
        details = request.POST.get('details')

        club = BookClub.objects.create(
            group_name=group_name,
            book_photo=book_photo,
            book_title=book_title,
            book_author=book_author,
            date=date,
            time=time,
            city_location=city_location,
            district_location=district_location,
            dong_location=dong_location,
            discussion_field=discussion_field,
            discussion_keywords=discussion_keywords,
            min_members=min_members,
            max_members=max_members,
            details=details
        )

        context = {'club_id': club.id}
        return render(request, 'club/create_success.html', context)

    return render(request, 'club/create.html')

# 독서 모임 신청
def apply_club(request, club_id): # , user_id
    if request.method == 'POST':
        club = get_object_or_404(BookClub, id=club_id)

        # 최대 멤버 수 초과하는지 확인
        if club.applied_members < club.max_members:
            applied_members = request.POST.get('applied_members')
            # 신청 멤버 수 update
            club = BookClub.objects.update(
                applied_members=applied_members+1
            )

            context = {'club_id': club.id}
            return render(request, 'club/apply_success.html', context)

    return render(request, 'club/club_detail.html')