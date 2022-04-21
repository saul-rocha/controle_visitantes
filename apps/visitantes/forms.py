from django import forms
from visitantes.models import Visitante

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = [
            "nome_completo", "cpf", "data_nascimento",
            "numero_casa", "placa_veiculo"
        ]

        error_messages = {
            "nome_completo": {
                "required": "Nome completo é obrigatório"
            },
            "cpf": {
                "required": "CPF é obrigatório"
            },
            "data_nascimento": {
                "required": "Data de nascimento é obrigatória", 
                "invalid":"Por favor, informe uma data válida (DD/MM/AAAA)"
            },
            "numero_casa": {
                "required": "Informe o numero da casa a ser visitada"
            },
        }

class AutorizaVisitanteForm(forms.ModelForm):

    morador_reponsavel = forms.CharField(required=True)


    class Meta:
        model = Visitante
        fields = [
            "morador_responsavel"
        ]

        error_messages = {
            "morador_responsavel": {
                "required": "Por favor, informe o nome do morador responsável por autorizar a entrada do visitante"
            }
        }