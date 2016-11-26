from django.contrib.auth.models import Permission, User
from django.db import models


class Album(models.Model):
    user = models.ForeignKey(User, default=1)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
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
    user_id = models.BigIntegerField()
    state_id = models.IntegerField()
    country_id = models.IntegerField()
    city_id = models.IntegerField()
    zip_id = models.IntegerField()
    zip_id2 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Addresses'


class Affiliates(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Affiliates'


class Amazon(models.Model):
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    apikey = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Amazon'


class Emails(models.Model):
    id = models.BigIntegerField(primary_key=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    primary = models.IntegerField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Emails'


class Facebook(models.Model):
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    apikey = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Facebook'


class Gamegifts(models.Model):
    id = models.BigIntegerField(primary_key=True)
    game = models.ForeignKey('Games', models.DO_NOTHING)
    gift = models.ForeignKey('Gifts', models.DO_NOTHING)
    times_stolen = models.IntegerField()
    current_user = models.ForeignKey('Users', models.DO_NOTHING, related_name = 'current_user_id')
    purchased_user = models.ForeignKey('Users', models.DO_NOTHING, related_name = 'purchased_user_id')
    selected_user = models.ForeignKey('Users', models.DO_NOTHING, related_name = 'selected_user_id')
    gift_type = models.ForeignKey('Gifttypes', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'GameGifts'


class Games(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    starttime = models.DateTimeField()
    status = models.ForeignKey('Status', models.DO_NOTHING, db_column='status')
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by')
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Games'


class Gifttrails(models.Model):
    id = models.BigIntegerField(primary_key=True)
    giftid = models.ForeignKey('Gifts', models.DO_NOTHING, db_column='giftid')
    user = models.ForeignKey('Users', models.DO_NOTHING)
    game = models.ForeignKey(Games, models.DO_NOTHING)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'GiftTrails'


class Gifttypes(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'GiftTypes'


class Gifts(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    price = models.ForeignKey('Prices', models.DO_NOTHING)
    affiliate = models.ForeignKey(Affiliates, models.DO_NOTHING)
    type = models.ForeignKey(Gifttypes, models.DO_NOTHING)
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


class Google(models.Model):
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    apikey = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Google'


class Integrations(models.Model):
    name = models.CharField(max_length=45)
    table_name = models.CharField(max_length=45)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Integrations'


class Logins(models.Model):
    id = models.BigIntegerField(primary_key=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=40, blank=True, null=True)
    attempt = models.IntegerField()
    status = models.ForeignKey('Status', models.DO_NOTHING)
    datetime = models.DateTimeField()
    ipaddress = models.CharField(max_length=15)
    useragent = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Logins'


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
    type = models.ForeignKey(Notificationtypes, models.DO_NOTHING)
    from_user = models.ForeignKey('Users', models.DO_NOTHING, related_name = 'from_user_id')
    to_user = models.ForeignKey('Users', models.DO_NOTHING, related_name = 'to_user_id')
    status = models.ForeignKey('Status', models.DO_NOTHING)
    message = models.ForeignKey(Messages, models.DO_NOTHING)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Notifications'


class Passwords(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    password = models.CharField(max_length=40)
    previous_password = models.CharField(max_length=40)
    last_changed = models.DateTimeField()
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Passwords'


class Paypal(models.Model):
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    apikey = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Paypal'


class Phonenumbers(models.Model):
    id = models.BigIntegerField(primary_key=True)
    phone_number = models.CharField(max_length=13)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'PhoneNumbers'


class Players(models.Model):
    id = models.BigIntegerField(primary_key=True)
    clock = models.IntegerField()
    user = models.ForeignKey('Users', models.DO_NOTHING)
    game = models.ForeignKey(Games, models.DO_NOTHING)
    status = models.ForeignKey('Status', models.DO_NOTHING)
    gift = models.ForeignKey(Gifts, models.DO_NOTHING)
    turn_number = models.IntegerField()
    role = models.ForeignKey('Roles', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Players'


class Playersmoods(models.Model):
    id = models.IntegerField(primary_key=True)
    game = models.ForeignKey(Games, models.DO_NOTHING)
    player = models.ForeignKey(Players, models.DO_NOTHING, blank=True, null=True)
    mood = models.ForeignKey(Moods, models.DO_NOTHING, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PlayersMoods'


class Prices(models.Model):
    id = models.IntegerField(primary_key=True)
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
    status = models.CharField(max_length=20)

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


class Twitter(models.Model):
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    apikey = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Twitter'


class Usps(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'USPS'


class Users(models.Model):
    id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    nick_name = models.CharField(max_length=45, blank=True, null=True)
    profile_image = models.CharField(max_length=45)
    role = models.ForeignKey(Roles, models.DO_NOTHING)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Users'

