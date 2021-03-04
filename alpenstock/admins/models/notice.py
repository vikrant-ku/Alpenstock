from django.db import models

class Notices(models.Model):
    recipient = models.CharField(max_length=10, default='All')
    type = models.CharField(max_length=10, default='Holiday')
    date = models.DateField()
    notice = models.TextField()

    def __str__(self):
        return self.recipient
