from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import ProfileForm ,ProjetForm
from django.db.models import Prefetch
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):#good
    online=''
    projet=Projet.objects.all().order_by('-date')
    profile=Profile.objects.all().order_by('-date_added')
    if request.user is not None and request.user.is_authenticated:
        online=Profile.objects.get(user=request.user)
    else:
        ''
    """paginator=Paginator(profile,4)
    page=request.GET.get('page')
    profile=paginator.get_page(page)

    paginasyon=Paginator(projet,3)
    page=request.GET.get('page')
    projet=paginasyon.get_page(page)"""

    context={
        'profile':profile,
        'projet':projet,
        'online':online
    }
    return render(request,'index.html',context)

def newuser(request):#good
    if request.method== 'POST':
        username=request.POST.get('nom')
        modpas=request.POST.get('modpas')
        confirm=request.POST.get('confirm')
        if User.objects.filter(username = username).first():
            messages.error(request, "This username is already taken")
            return redirect(newuser)
        if modpas !=confirm:
            messages.error(request,('verifier bien votre mot de passe'))
        else:
            user=User.objects.create_user(username=username,password=modpas)
            login(request,user)
            return redirect(index)
    return render(request,'newUser.html')


def connect(request):#good
    if request.method =='POST':
        username=request.POST['nom']
        modpas=request.POST['modpas']
        user=authenticate(username=username,password=modpas)
        if user is not None:
            login(request,user)
            return redirect(index)

    return render(request,'loge.html')


def deconect(request):
    logout(request)
    return redirect(index)

@login_required(login_url='login')
def newproject(request):
    online=''
    if request.user is not None and request.user.is_authenticated:
        online=Profile.objects.get(user=request.user)
    else:
        '' 
    if request.method=='POST':
        projet_form=ProjetForm(data=request.POST,files=request.FILES)
        if projet_form.is_valid():
            new=projet_form.save(commit=False)
            new.user=request.user
            new.save()
            messages.success(request,('vous venez d\'ajouter un nouveau projet'))
            return redirect(readprojet,id=new.pk)
        else:
            messages.success(request,('vous venez d\'ajouter un nouveau projet'))

        return redirect(index)
    projet_form=ProjetForm( )   
    context={
        'projet_form':projet_form,
        'online':online
    }
    return render(request,'newproject.html',context)

def readprojet(request,id):
    online=''
    proje=Projet.objects.prefetch_related(Prefetch('categori')).filter(id=id)
    if request.user is not None and request.user.is_authenticated:
        online=Profile.objects.get(user=request.user)
    else:
        '' 
    context={
        'proje':proje,
        'online':online
    }
    return render(request,'readproje.html',context)


def unprofile(request,id):
    online=''
    personal=User.objects.select_related('profile').prefetch_related(Prefetch('projet_set',queryset=Projet.objects.all())).filter(id=id)
    if request.user is not None and request.user.is_authenticated:
        online=Profile.objects.get(user=request.user)
    else:
        '' 
         
    context={
        'personal':personal,
        'online':online
    }
    return render(request,'profile.html',context)

@login_required(login_url='login')
def myprofile(request):
    if request.user is not None:
        profile=Profile.objects.get(user=request.user)
        proje_yo=Projet.objects.filter(user=request.user)
        
    if request.method =='POST':
        profil_form=ProfileForm(request.POST, request.FILES,instance=request.user.profile)
        if profil_form.is_valid():
            profil_form.save()
            messages.success(request,'your profile is updated with successfull')
            return redirect(myprofile)
    else:
        profil_form=ProfileForm(instance=request.user.profile)        
    context={
        'profile':profile,
        'profil_form':profil_form,
        'proje_yo':proje_yo
    }
    return render(request,'myprofil.html',context)


@login_required(login_url='login')
def efaseproje(request,id):
    if request.user is not None:
        referer_url=request.META.get('HTTP_REFERER', '/')
        trash=Projet.objects.filter(id=id)
        trash.delete()

    return redirect(referer_url)


def toutproje(request):
    online=''
    if request.user is not None and request.user.is_authenticated:
        online=Profile.objects.get(user=request.user)
    else:
        '' 
    tout_proje=Projet.objects.all()
    context={
        'tout_proje':tout_proje,
        'online':online
    }
    return render(request,'toutproje.html',context)

def toutprofil(request):
    online=''
    if request.user is not None and request.user.is_authenticated:
        online=Profile.objects.get(user=request.user)
    else:
        '' 
    tout_profil=Profile.objects.all()
    context={
        'tout_profil':tout_profil,
        'online':online
    }
    return render(request,'toutprofil.html',context)
"""
li yon proje ### OK
efase yon proje si se itilizate an ki te kreyel ##OK
li proje yon moun pandan ou antre ladan an ...###OK
"""