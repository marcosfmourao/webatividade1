# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-09 00:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaConta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataVencimento', models.DateTimeField(verbose_name='data vencimento')),
                ('dataPagamento', models.DateTimeField(verbose_name='data pagamento')),
                ('valorAPagar', models.FloatField()),
                ('valorPago', models.FloatField(default=0)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.CategoriaConta')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='contas.Pessoa')),
                ('CPF', models.CharField(max_length=20)),
            ],
            bases=('contas.pessoa',),
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='contas.Pessoa')),
                ('CNPJ', models.CharField(max_length=20)),
            ],
            bases=('contas.pessoa',),
        ),
        migrations.AddField(
            model_name='conta',
            name='credor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.PessoaJuridica'),
        ),
        migrations.AddField(
            model_name='conta',
            name='devedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.PessoaFisica'),
        ),
    ]