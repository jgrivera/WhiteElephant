from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import GameForm, SongForm, UserForm
from .models import Game, Song
# for mobile web
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, loader

AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def profile(request):
    if not request.user.is_authenticated():
        return render(request, 'game/login.html')
    else:
        user = request.user
        userprofile = get_object_or_404(Game, pk=request.user)
        return render(request, 'game/detail.html', {'game': userprofile, 'user': uid})


def create_game(request):
    if not request.user.is_authenticated():
        return render(request, 'game/login.html')
    else:
        form = GameForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            game = form.save(commit=False)
            game.user = request.user
            # album.album_logo = request.FILES['album_logo']
            # file_type = album.album_logo.url.split('.')[-1]
            # file_type = file_type.lower()
            # if file_type not in IMAGE_FILE_TYPES:
            #     context = {
            #         'album': album,
            #         'form': form,
            #         'error_message': 'Image file must be PNG, JPG, or JPEG',
            #     }
            #     return render(request, 'game/create_game.html', context)
            game.save()
            return render(request, 'game/detail.html', {'game': game})
        context = {
            "form": form,
        }
        return render(request, 'game/create_game.html', context)


def create_song(request, game_id):
    form = SongForm(request.POST or None, request.FILES or None)
    game = get_object_or_404(Game, pk=game_id)
    if form.is_valid():
        games_songs = game.song_set.all()
        for s in games_songs:
            if s.song_title == form.cleaned_data.get("song_title"):
                context = {
                    'game': game,
                    'form': form,
                    'error_message': 'You already added that song',
                }
                return render(request, 'game/create_song.html', context)
        song = form.save(commit=False)
        song.game = game
        song.audio_file = request.FILES['audio_file']
        file_type = song.audio_file.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in AUDIO_FILE_TYPES:
            context = {
                'game': game,
                'form': form,
                'error_message': 'Audio file must be WAV, MP3, or OGG',
            }
            return render(request, 'game/create_song.html', context)

        song.save()
        return render(request, 'game/detail.html', {'game': game})
    context = {
        'game': game,
        'form': form,
    }
    return render(request, 'game/create_song.html', context)


def delete_game(request, game_id):
    game = Game.objects.get(pk=game_id)
    game.delete()
    games = Game.objects.filter(user=request.user)
    return render(request, 'game/index.html', {'games': games})


def delete_song(request, game_id, song_id):
    game = get_object_or_404(Game, pk=game_id)
    song = Song.objects.get(pk=song_id)
    song.delete()
    return render(request, 'game/detail.html', {'game': game})


def detail(request, game_id):
    if not request.user.is_authenticated():
        return render(request, 'game/login.html')
    else:
        user = request.user
        game = get_object_or_404(Game, pk=game_id)
        return render(request, 'game/detail.html', {'game': game, 'user': user})


def favorite(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    try:
        if song.is_favorite:
            song.is_favorite = False
        else:
            song.is_favorite = True
        song.save()
    except (KeyError, Song.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})


def favorite_game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    try:
        if game.is_favorite:
            game.is_favorite = False
        else:
            game.is_favorite = True
        game.save()
    except (KeyError, Game.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})



def index(request):

    if not request.user.is_authenticated():
        return render(request, 'game/login.html')
    else:
        games = Game.objects.filter(user=request.user)
        song_results = Song.objects.all()
        query = request.GET.get("q")
        if query:
            games = games.filter(
                Q(game_title__icontains=query) |
                Q(artist__icontains=query)
            ).distinct()
            song_results = song_results.filter(
                Q(song_title__icontains=query)
            ).distinct()
            return render(request, 'game/index.html', {
                'games': games,
                'songs': song_results,
            })
        else:
            return render(request, 'game/index.html', {'games': games})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'game/login.html', context)

def policyandagreement(request):
    return render(request, 'game/policyandagreement.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                games = Game.objects.filter(user=request.user)
                return render(request, 'game/index.html', {'games': games})
            else:
                return render(request, 'game/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'game/login.html', {'error_message': 'Invalid login'})
    return render(request, 'game/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                games = Game.objects.filter(user=request.user)
                return render(request, 'game/index.html', {'games': games})
    context = {
        "form": form,
    }
    return render(request, 'game/register.html', context)


def friends(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'game/login.html')
    else:
        try:
            song_ids = []
            for game in Game.objects.filter(user=request.user):
                for song in game.song_set.all():
                    song_ids.append(song.pk)
            users_songs = Song.objects.filter(pk__in=song_ids)
            if filter_by == 'favorites':
                users_songs = users_songs.filter(is_favorite=True)
        except Game.DoesNotExist:
            users_songs = []
        return render(request, 'game/friends.html', {
            'song_list': users_songs,
            'filter_by': filter_by,
        })
