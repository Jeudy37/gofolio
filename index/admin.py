from django.contrib import admin
from .models import *
# Register your models here.

class AdminProfile(admin.ModelAdmin):
    list_display=('user','nom','siyati','email','telefon','date_added')


class AdminProjet(admin.ModelAdmin):
    list_display=('user','titre','date')

class AdminKategori(admin.ModelAdmin):
    list_display=('nom',)

admin.site.register(Profile,AdminProfile)
admin.site.register(Projet,AdminProjet)
admin.site.register(Kategori,AdminKategori)

