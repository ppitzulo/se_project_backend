from django.db import models

# Create your models here.
class Score(models.Model):
    user_id = models.CharField(max_length=10)
    score = models.FloatField()

    class Meta:
        db_table = "score"