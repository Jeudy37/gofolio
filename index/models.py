from django.db import models
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import post_save
import random
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    nom=models.CharField(max_length=200 ,null=True,)
    siyati=models.CharField(max_length=200, null=True)
    email=models.EmailField(max_length=100, null=True)
    telefon=models.CharField(max_length=40, null=True, blank=True)
    foto=models.ImageField(upload_to='my_picture/', blank=True, null=True)
    date_added=models.DateTimeField(auto_now=True)

    @receiver(post_save, sender=User)
    def user_profile(sender,instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def user_profile(sender, instance ,**kwargs):
        instance.profile.save()
    
    class Meta:
        ordering=['-date_added']

    def __str__(self):
        return str(self.user)
    

class Kategori(models.Model):
    kate=(
        ('design','design'),
         ('food','food'),
         ('education','education'),
         ('energy','energy'),
         ('technology','technology'),
         ('programming','programming'),
         ('health','health'),
         ('finance','finance'),
         ('money','money') 
    )
    nom=models.CharField(max_length=150, choices=kate)
    def __str__(self):
        return self.nom


# Create your models here

class Projet(models.Model):
    categori=models.ManyToManyField(Kategori ,blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    slug=models.SlugField(max_length=200,unique=True)
    titre=models.CharField(max_length=200, blank=True, null=True)
    description=models.TextField(max_length=5000, blank=True)
    date=models.DateTimeField(auto_now_add=True)
    foto=models.ImageField(upload_to='image/',blank=True)

    def save(self, *args,**kwargs) :
        if self.pk is None:
            slug_m= slugify(self.titre)
            while Projet.objects.filter(slug=slug_m):
                slug_m+=str(random.randrange(1,2500))
            self.slug=slug_m
        super(Projet,self).save(args,kwargs)

    def __str__(self):
        return self.titre
