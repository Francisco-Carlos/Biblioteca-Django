from django import forms
from django.contrib.auth.models import User
from .models import Livro,Editora,Reservar

class Create_reser(forms.ModelForm):
    class Meta:
        model = Reservar
        fields = ["Nome","Nome_liv","Devolver"]
        widgets ={
            'Nome': forms.Select(attrs={'class':'form-control'}),
            'Nome_liv':forms.Select(attrs={'class':'form-control'}),
            'Devolver':forms.DateInput(attrs={'class':'form-control'}),
        }


class Create_livr(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ["Id_Li","Nome","Autor","Resumo","Observacao","Imag","Editora"]
        widgets = {
            'Id_Li':forms.TextInput(attrs={'class':'form-control'}),
            'Nome':forms.TextInput(attrs={'class':'form-control'}),
            'Autor':forms.TextInput(attrs={'class':'form-control'}),
            'Observacao':forms.TextInput(attrs={'class':'form-control'}),
            'Resumo':forms.Textarea(attrs={'class':'form-control'}),
            'Editora':forms.Select(attrs={'class':'form-control'}),
            'Imag':forms.FileInput(attrs={'class':'form-control'}),

        }


#criando usuarios
class Craete_User(forms.Form):
    Username = forms.CharField(label='Entre com o seu Nome',min_length=4,max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    Email = forms.EmailField(label='digite seu email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    Passaword1 = forms.CharField(label='digte sua senha',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    Passaword2 = forms.CharField(label='confirmar senha',widget=forms.PasswordInput(attrs={'class':'form-control'}))



    def save(self,commit=True):
        user = User.objects.create_user(
            self.cleaned_data['Username'],
            self.cleaned_data['Email'],
            self.cleaned_data['Passaword1'],
        )
        return user
