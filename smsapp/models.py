from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField("First name", max_length=255, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    subject = models.CharField("subject", max_length=50, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name 