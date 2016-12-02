from django import forms
from django.contrib.auth.models import User

from .models import Game, Song


class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        # fields = ['artist', 'album_title', 'genre', 'album_logo']
        fields = ['game_name', 'game_start_time', 'gift_price', 'number_of_joke_gifts']


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['song_title', 'audio_file']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
