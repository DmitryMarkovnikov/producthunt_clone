from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):

    def __str__(self):
        return self.title

    title = models.CharField(max_length=255)
    body = models.TextField()
    url = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def summary(self):
        return "{} ...".format(self.body[:100])

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')