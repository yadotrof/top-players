from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100,
                            help_text="Player name",
                            null=False,
                            blank=False)
    highscore = models.IntegerField(default=0,
                                    help_text="Player highscore")

    @property
    def position(self):
        aggregate = (Player.objects.filter(highscore__gt=self.highscore)
                           .values('highscore')
                           .distinct())
        return len(aggregate) + 1
