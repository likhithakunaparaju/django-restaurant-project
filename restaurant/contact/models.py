from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    review=models.TextField()

    def __str__(self):
        self.name
