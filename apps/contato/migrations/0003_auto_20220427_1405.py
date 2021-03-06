# Generated by Django 3.0 on 2022-04-27 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contato', '0002_auto_20220427_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='assunto',
            field=models.CharField(choices=[('D', 'Dúvida'), ('C', 'Crítica'), ('A', 'Ajuda'), ('S', 'Sugestão')], default='S', max_length=1, verbose_name='Assunto'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='mensagem',
            field=models.TextField(verbose_name='Mensagem'),
        ),
    ]
