from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Food(models.Model) :
    title = models.CharField(max_length=100,verbose_name='水果名')
    description = models.CharField(max_length=250,verbose_name='水果简介')
    image = models.ImageField(upload_to='food/images/',verbose_name='水果海报')
    url = models.URLField(blank=True,verbose_name='水果链接')

    class Meta:
        verbose_name='水果'
        verbose_name_plural='水果'

    def __str__(self):
        return self.title

class Review(models. Model) :
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    watchAgain = models.BooleanField()
    def __str__(self) :
        return self.text