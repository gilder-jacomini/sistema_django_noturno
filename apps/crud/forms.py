from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'cpf', 'email', 'telefone', 'data_nascimento', 'sintomas']
        widgets = {
            'nome':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id':"nome",
                    'required':True,
                },
            ),
            'cpf':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id':"cpf",
                    'required':True,
                },
            ),
            'email':forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'id':"email",
                    'required':True,
                },
            ),
            'telefone':forms.TelInput(
                attrs={
                    'class':'form-control',
                    'id':"telefone",
                    'required':True,
                },
            ),
            'data_nascimento':forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'class':'form-control',
                    'id':"data_nascimento",
                    'required':True,
                    'type':'date',
                },
            ),
            'sintomas':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'id':"sintomas",
                    'rows': 3,
                },
            ),
        }
        error_messages = {
            'email': {
                'unique': "Este email já está em uso.",
            },
            'cpf': {
                'unique': "Este CPF já está em uso.",
            },
        }
