from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

from .forms import UserCreateForm, SignUpForm

def signup_view(request):
    # GET 요청 시 HTML 응답
    if request.method == 'GET':
        form = SignUpForm
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        # POST 요청 시 데이터 확인 후 회원 생성
        form = SingUpForm(request.POST)

        if form.is_valid():
            # 회원가입 처리
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password2 = form.cleaned_data['password2']

        else:
            # 리다이렉트
            return redirect('accounts:signup')

# , AuthenticationForm
# from django.contrib.auth import login, logout
#             instance = form.save()
#             return redirect('index')

from django.contrib.auth.decorators import login_required
@login_required
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')
