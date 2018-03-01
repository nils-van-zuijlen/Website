from django.utils import timezone
from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group


class Killer(models.Model):
    registration_start_date = models.DateTimeField()
    registration_end_date = models.DateTimeField()
    game_start_date = models.DateTimeField()
    game_end_date = models.DateTimeField()
    
    def __str__(self):
        return "{} - {}".format(self.game_start_date.isoformat(), self.game_end_date.isoformat())

    def is_registration_open(self):
        return self.registration_start_date <= timezone.now() <= self.registration_end_date

    def is_registration_ended(self):
        return timezone.now() >= self.registration_end_date

    def is_creation_in_progress(self):
        return self.registration_end_date <= timezone.now() <= self.game_start_date

    def is_game_open(self):
        return self.game_start_date <= timezone.now() <= self.game_end_date

    def is_game_ended(self):
        return timezone.now() >= self.game_end_date

class Participant(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='participating_killers'
        )
    game = models.ForeignKey(Killer)
    killing = models.OneToOneField(
        'Participant',
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={'killing': None},
        related_name='killed_by'
        )
    dead = models.BooleanField(default=False)

    def is_alive(self):
        return not self.dead

    def fire(self):
        self.killing.kill()

    def kill(self):
        self.dead = True
