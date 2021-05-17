from django.db import models
from note.models import Note


class Calendar(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    note = models.ForeignKey(Note, on_delete=models.CASCADE)