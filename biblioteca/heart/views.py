from django.shortcuts import render,redirect
from .models import Livro,Editora,Reservar
from .form import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# para login,logout,e index e criar usuario

def Index(request):
    return render(request,'index.html')

def Usuario(request):
    users = User.objects.all()
    return render(request,'Usuario.html',{'users':users})

def Login(request):
    return render(request,'login.html')

def Login_user(request):
    if request.POST:
        usern = request.POST.get('username')
        passw = request.POST.get('password')
        user = authenticate(username=usern,password=passw)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,'usuario ou senha errado')
    return redirect('/heart/login/')

def Logout(request):
    request(logout)
    return redirect('/heart/login/')

def Deletar_user(request,id):
    users = User.objects.get(id=id)
    users.delete()
    return redirect('/')


# criar user
def Cadastrar_User(request):
    if request.POST:
        cads = Craete_User(request.POST)
        if cads.is_valid():
            cads.save()
            messages.success(request,'criado com sucesso')
            return redirect('/heart/user/')
    else:
        cads = Craete_User()
    return render(request,'Cadastrar_User.html',{'cads':cads})
# paginas da biblioteca
def Livros_lis(request):
    livros = Livro.objects.all()
    return render(request,'Livro.html',{'livros':livros})
# Create your views here.

def Editoras_lis(request):
    editoras = Editora.objects.all()
    return render(request,'Editora.html',{'editoras':editoras})
def Reservar_lis(request):
    reservas = Reservar.objects.all()
    return render(request,'Reservar.html',{'reservas':reservas})

''' detalhes de todos '''
def Detalhes_liv(request,id):
    lista = Livro.objects.get(id=id)
    return render(request,'detalhes.html',{'lista':lista})

def Detalhes_res(request,id):
    reserva = Reservar.objects.get(id=id)
    return render(request,'detalhes_rev',{'reserva':reserva})

def Detalhes_Edi(request,id):
    editora =Editora.objects.get(id=id)
    test = Livro.objects.all()
    return render(request,'detalhes_Edi.html',{'editora':editora})

''' Cadastro livro'''



def Formulario_liv(request):
    if request.method == 'POST':
        form = Create_livr(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/heart/livros/')
    else:
        form = Create_livr()
    return render(request,'cadastrar_liv.html',{'form':form})
def Livros_reg(request):
    livro = request.GET.get('id')
    if livro:
        lista = Livro.objects.get(id=livro)
        test = Editora.objects.all()
        return render(request,'editar.html',{'lista':lista})
    return render(request,'editar.html')

def Editora_reg(request):
    editora = request.GET.get('id')
    if editora:
        lista = Editora.objects.get(id=editora)
        return render(request,'cadastrar.html',{'editora':lista})
    return render(request,'cadastrar.html')


def Reserva_reg(request):
    reserva = request.GET.get('id')
    reservar = Reservar.objects.all()
    if reserva:
        reserva = Reservar.objects.get(id=reserva)
        return render(request,'Cadastrar_res.html',{'reserva':reserva})
    return render(request,'Cadastrar_res.html',{'reservar':reservar})
''' Cadastrar e Editar e Excluir'''
def Editar_liv(request):
    nom = request.POST.get('titulo')
    aut = request.POST.get('autor')
    ob = request.POST.get('observacao')
    resu = request.POST.get('resumo')
    ima = request.FILES.get('image')
    user = request.user
    livro_id = request.POST.get('livro_id')
    if livro_id:
        livro = Livro.objects.get(id=livro_id)
        livro.Nome = nom
        livro.Autor = aut
        livro.Observacao = ob
        livro.Resumo = resu
        if ima:
            livro.Imag = ima
        livro.save()
    else:
        livro = Livro.objects.create(Nome=nom,Autor=aut,Observacao=ob,Resumo=resu,Imag=ima)
    url = f'/heart/detalhes/{livro.id}/'
    return redirect(url)

def Deletar_liv(request,id):
    livro = Livro.objects.get(id=id)
    livro.delete()
    return redirect('/')

'''Cadastrar e excluir e editar da Editora'''
def Cadastrar_edi(request):
    ids = request.POST.get('ids')
    nom = request.POST.get('nome')
    end = request.POST.get('endereco')
    tel = request.POST.get('telefone')
    sit = request.POST.get('site')
    editora_id =request.POST.get('editora_id')
    if editora_id:
        editora = Editora.objects.get(id=editora_id)
        editora.Id_Ed = ids
        editora.Nome = nom
        editora.Edereco = end
        editora.Telefone = tel
        editora.Site = sit
        editora.save()
    else:
        editora = Editora.objects.create(Id_Ed=ids,Nome=nom,Edereco=end,Telefone=tel,Site=sit)
    url =f'/heart/detalhes_Edi/{editora.id}/'
    return redirect(url)

def Deletar_edi(request,id):
    editora = Editora.objects.get(id=id)
    editora.delete()
    return redirect('/')

'''cadstar editar excluir '''
@login_required(login_url='/heart/login/')
def Formulario_res(request,):
    if request.method == 'POST':
        form = Create_reser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/heart/reserva/')
    else:
        form = Create_reser()
    return render(request,'Form_res.html',{'form':form})

def Cadastrar_res(request):
    non = request.POST.get('nome')
    liv = request.POST.get('livro')
    dev = request.POST.get('data')
    reservar_id = request.POST.get('reserva_id')
    if reservar_id:
        reservar = Reservar.objects.get(id=reservar_id)
        reservar.Nome = non
        reservar.Nome_liv = liv
        reservar.Devolver = dev
        reservar.save()
    else:
        return redirect('/heart/cadastrar_res/')



def Deletar_res(request,id):
    reservar = Reservar.objects.get(id=id)
    reservar.delete()
    return redirect('/')