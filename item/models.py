from django.db import models
from django.urls import reverse

# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length=255)
    call = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item:account_detail', kwargs={'pk':self.pk})

#
class Item(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()
    content = models.TextField(null=True)
    price = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE, db_column='name')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('item:item_detail', kwargs={'pk':self.pk})