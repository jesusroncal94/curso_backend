from django.db import models
from django.utils import timezone


class Biography(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(
        blank=True, null=True)

    def __str__(self):
        return self.person
