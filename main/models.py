from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=500)
    def __str__(self) -> str:
        return self.name
class Worker(models.Model):
    category = models.ForeignKey(Category, verbose_name="categoriya tanlang", on_delete=models.CASCADE)
    name = models.CharField(max_length=500,verbose_name = "Ism va Familiya Kiriting")
    age = models.IntegerField(verbose_name='Yoshingiz')
    portfolio_website = models.CharField(max_length=500,verbose_name = "Agar Portfolio web sitegiz bo`lsa urlni kiriting",default='none')
    telegram = models.CharField(max_length=500,verbose_name = "Telegram nomingiz yoki telefon raqamingizni qoldiring",default='none')
    instagram = models.CharField(max_length=500,verbose_name = "Instagram nomingiz yoki telefon raqamingizni qoldiring",default='none')
    preum = models.BooleanField(max_length=500,default=False)
    more = models.TextField(verbose_name='iltimos o`zingiz haqingizda yozing!',default='none')
    image = models.FileField(upload_to='ramlar/',verbose_name='rasmingizni joylang')

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')
    