from django.db import models

class Contato(models.Model):
    email = models.EmailField(
        verbose_name="E-mail"
    )

    DUVIDA = 'D'
    CRITICA = 'C'
    AJUDA = 'A'
    SUGESTÃO = 'S'
    assuntos = [
        (DUVIDA, 'Dúvida'),
        (CRITICA, 'Crítica'),
        (AJUDA, 'Ajuda'),
        (SUGESTÃO, 'Sugestão'),
    ]

    assunto = models.CharField(
        verbose_name="Assunto",
        max_length=1,
        choices=assuntos,
        default=SUGESTÃO,
    )

    mensagem = models.TextField(
        verbose_name="Mensagem"
    )

    def __str__(self):
        return self.email


