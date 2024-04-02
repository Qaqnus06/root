from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Book(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    image = models.ImageField(upload_to='book_images/')
    tillar=models.ForeignKey('Til',on_delete=models.CASCADE,related_name='til')
    

    def __str__(self):
        return self.name
    
class Til(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name   

class Ega(models.Model):
    first_name=models.CharField(max_length=200)   
    last_name=models.CharField(max_length=200)
    age=models.IntegerField(null=True,blank=True)
    gender=models.CharField(max_length=200,null=True,blank=True)
    email=models.CharField(max_length=200,null=True,blank=True)
    phone=models.CharField(max_length=200,null=True,blank=True)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Muallif"
        verbose_name_plural = "Mualliflar"


class KitobEga(models.Model):
    kitob=models.ForeignKey(Book,on_delete=models.CASCADE)  
    ega=models.ForeignKey(Ega,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.kitob} owned by {self.ega}"

class Comment(models.Model):
    user=models.ForeignKey('users.User', on_delete=models.CASCADE)
    kitob=models.ForeignKey(Book,on_delete=models.CASCADE,related_name="izohlar")
    comment_text=models.TextField()
    stars_given=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    created_at=models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.user} Useri tomonidan {self.kitob.name} kitobiga {self.stars_given} yulduz qoyildi"
    
    class Meta:
        verbose_name = "Komentariya"
        verbose_name_plural = "Komentariyalar"
     