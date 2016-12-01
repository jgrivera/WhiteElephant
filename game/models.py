from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User

from django.db import models

import allauth.app_settings

class Album(models.Model):
    user = models.ForeignKey(User, default=1)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    game_name = models.CharField(max_length=500)
    game_start_time = models.CharField(max_length=500)
    gift_price = models.CharField(max_length=500)
    number_of_joke_gifts = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
#  Models for WhiteElephant



class Addresses(models.Model):
    address_1 = models.CharField(max_length=45)
    address_2 = models.CharField(max_length=45, blank=True, null=True)
    user_id = models.ForeignKey(allauth.app_settings.USER_MODEL, on_delete=models.CASCADE)
    state_id = models.IntegerField()
    country_id = models.IntegerField()
    city_id = models.IntegerField()
    zip_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Addresses'


class Affiliates(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Affiliates'


class Countries(models.Model):
    iso = models.CharField(max_length=2)
    name = models.CharField(max_length=80)
    nicename = models.CharField(max_length=80)
    iso3 = models.CharField(max_length=3, blank=True, null=True)
    numcode = models.SmallIntegerField(blank=True, null=True)
    phonecode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Countries'


class Emails(models.Model):
    email = models.CharField(max_length=100)
    user_id = models.ForeignKey(allauth.app_settings.USER_MODEL, on_delete=models.CASCADE)
    primary = models.IntegerField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Emails'


class Gamegifts(models.Model):
    id = models.BigIntegerField(primary_key=True)
    game_id = models.ForeignKey('Games', models.DO_NOTHING)
    gift_id = models.ForeignKey('Gifts', models.DO_NOTHING)
    times_stolen = models.IntegerField(default=0)
    current_user_id = models.ForeignKey(allauth.app_settings.USER_MODEL, on_delete=models.DO_NOTHING, related_name='current_user_id')
    purchased_user_id = models.ForeignKey(allauth.app_settings.USER_MODEL, on_delete=models.DO_NOTHING, related_name='purchased_user_id')
    selected_user_id = models.ForeignKey(allauth.app_settings.USER_MODEL, on_delete=models.DO_NOTHING,related_name='selected_user_id')
    gift_type_id = models.ForeignKey('Gifttypes', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'GameGifts'


class Games(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    starttime = models.DateTimeField()
    status_id = models.ForeignKey('Status', models.DO_NOTHING)
    created_by_id = models.ForeignKey(allauth.app_settings.USER_MODEL,
                             on_delete=models.DO_NOTHING)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Games'


class Gifttrails(models.Model):
    id = models.BigIntegerField(primary_key=True)
    gift_id = models.ForeignKey('Gifts', models.DO_NOTHING)
    user_id = models.ForeignKey(allauth.app_settings.USER_MODEL,  on_delete=models.DO_NOTHING)
    game_id = models.ForeignKey(Games, models.DO_NOTHING)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'GiftTrails'


class Gifttypes(models.Model):
    type = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'GiftTypes'


class Gifts(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    price_id = models.ForeignKey('Prices', models.DO_NOTHING)
    affiliate_id = models.ForeignKey(Affiliates, models.DO_NOTHING)
    type_id = models.ForeignKey(Gifttypes, models.DO_NOTHING)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Gifts'


class Github(models.Model):
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    url = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'GitHub'


class Integrations(models.Model):
    name = models.CharField(max_length=45)
    table_name = models.CharField(max_length=45)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Integrations'


class Messages(models.Model):
    id = models.BigIntegerField(primary_key=True)
    message = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Messages'


class Moods(models.Model):
    mood = models.CharField(max_length=45, blank=True, null=True)
    icon = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Moods'


class Notificationtypes(models.Model):
    type = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'NotificationTypes'


class Notifications(models.Model):
    type_id = models.ForeignKey(Notificationtypes, models.DO_NOTHING)
    from_user_id = models.ForeignKey(allauth.app_settings.USER_MODEL, on_delete=models.CASCADE, related_name="from_user_id")
    to_user_id = models.ForeignKey(allauth.app_settings.USER_MODEL, on_delete=models.CASCADE, related_name="to_user_id")
    status_id = models.ForeignKey('Status', models.DO_NOTHING)
    message = models.ForeignKey(Messages, models.DO_NOTHING)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Notifications'


class Phonenumbers(models.Model):
    phone_number = models.CharField(unique=True, max_length=13)
    user_id = models.ForeignKey(allauth.app_settings.USER_MODEL,on_delete=models.CASCADE)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'PhoneNumbers'


class Players(models.Model):
    id = models.BigIntegerField(primary_key=True)
    clock = models.DateTimeField()
    user_id = models.ForeignKey(allauth.app_settings.USER_MODEL, on_delete=models.DO_NOTHING, related_name="user_id")
    game_id = models.ForeignKey(allauth.app_settings.USER_MODEL, on_delete=models.DO_NOTHING, related_name="game_id")
    status_id = models.ForeignKey('Status', models.DO_NOTHING)
    gift_id = models.ForeignKey(Gifts, models.DO_NOTHING)
    turn_number = models.IntegerField()
    role_id = models.ForeignKey('Roles', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Players'


class Playersmoods(models.Model):
    game_id = models.BigIntegerField()
    player_id = models.ForeignKey(allauth.app_settings.USER_MODEL,  on_delete=models.CASCADE)
    mood_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PlayersMoods'


class Prices(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=5)

    class Meta:
        managed = False
        db_table = 'Prices'


class Roles(models.Model):
    role = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'Roles'


class Status(models.Model):
    status = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'Status'


class Twillio(models.Model):
    username = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    sid = models.CharField(max_length=45)
    auth_token = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Twillio'


class Usps(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'USPS'


class AccountEmailaddress(models.Model):
    email = models.CharField(unique=True, max_length=254)
    verified = models.IntegerField()
    primary = models.IntegerField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.CharField(max_length=128, blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.CharField(max_length=255)
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)
