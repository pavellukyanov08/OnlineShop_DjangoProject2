from .models import Profile
from django.forms import ModelForm


class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'username', 'email', 'img']

        labels = {
            'name': 'Имя:',
            'username': 'Пользователь:',
            'email': 'Почта:',
            'img': 'Фото профиля:'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'input'})