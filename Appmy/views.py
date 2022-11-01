from django.shortcuts import render, get_object_or_404, redirect
from .models import Contentt
from .forms import CommenttForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    postall = Contentt.objects.all().order_by('-new_date')
    
    context = {
        "postall":postall,
    }
    return render(request, "index.html", context)

def detail(request,id):
    postdetail = get_object_or_404(Contentt, id=id)
    
    form = CommenttForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = postdetail
        comment.save()
    
    context = {
        'postdetail':postdetail,
        'form':form,
    }
    return render(request, "detail.html", context)

def userLogin(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("index")
        else:
            context={
                "hata":"Kullanıcı adı veya parola yanlış!"
            }
            return render(request, "users/login.html", context)
            
    return render(request,"users/login.html")

def userRegister(request):
    
    if request.method == "POST":
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            user = User.objects.filter(username=username).exists()
            if user:
                return render(request,'users/register.html',{
                    "hata":"Bu kullanıcı adı daha önce alınmış!"
                })
            else:
                user = User.objects.create_user(username=username,password=password1, first_name=name, last_name = surname, email=email)
                user.save()
                return redirect("index")
        else:
            return render(request, 'users/register.html', {
                "hata": "Parolalar eşleşmiyor!"
            })
    return render(request,'users/register.html')

def userLogout(request):
    logout(request)
    return redirect('userLogin')
