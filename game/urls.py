from django.conf.urls import url
from . import views

app_name = 'game'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^game/$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^policyandagreement/$', views.policyandagreement, name='policyandagreement'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<game_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^friends/(?P<filter_by>[a-zA_Z]+)/$', views.friends, name='friends'),
    url(r'^create_game/$', views.create_game, name='create_game'),
    url(r'^(?P<game_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),
    url(r'^(?P<game_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
    url(r'^(?P<game_id>[0-9]+)/favorite_game/$', views.favorite_game, name='favorite_game'),
    url(r'^(?P<game_id>[0-9]+)/delete_game/$', views.delete_game, name='delete_game'),
    url(r'^profile/(?P<profile_id>[0-9]+)/$', views.profile, name='Profile'),
]
