from django.db import models
from users.models import CustomUser
from django.urls import reverse
from datetime import  datetime
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_create = models.DateField(auto_now_add=True)
    date_appoint = models.DateField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date_create}, {self.title}"

    @property
    def get_html_url(self):
        url = reverse('note:detail', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

    def get_absolute_url(self):
        return reverse('note:update', args=(self.id,))
