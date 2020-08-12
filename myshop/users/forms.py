from django.forms import ModelForm, EmailInput, PasswordInput, TextInput
from .models import User

class SignUpForm(ModelForm):
    class Meta:
        model = User # form에 사용할 모델 클래스
        fields = ['email', 'password', 'username', 'phone'] # form에 나타낼 필드

        labels = {
            'email': '이메일 주소',
            'password': '비밀번호',
            'username': '이름',
            'phone': '핸드폰 번호'
        }
        
        # form 속성 지정하기 위해 사용
        widgets = {
            'email': EmailInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'class': 'form-control'}),
            'username': TextInput(attrs={'class': 'form-control'}),
            'phone': TextInput(attrs={'class': 'form-control'})
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class SignInForm(ModelForm):
    class Meta:
        model = User
        exclude = ['username', 'phone']
        fields = ['email', 'password']
        labels = {
            'email': '이메일 주소',
            'password': '비밀번호',
        }
        widgets = {
            'email': EmailInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'class': 'form-control'})
        }

    def clean(self):
        cleaned_data = super().clean() # 부모에 있는 값을 clean으로 받아오기 
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        try:
            user = User.objects.get(pk=email)
            if not check_password(password, user.password):
                self.add_error('password', '비밀번호가 틀렸습니다.')
        except: # 없는 이메일(id)
            self.add_error('email', '가입하지 않은 이메일 주소입니다.')
