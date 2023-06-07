from django.db import models
from django.urls import reverse
from users.models import customUser


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(customUser, to_field='username', on_delete=models.SET('ANONYMOUS'), default='anonymous')
    body = models.TextField()
    access_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog', args=(self.pk,))

# Create your models here.
