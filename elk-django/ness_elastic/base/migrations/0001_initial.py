# Generated by Django 3.0.5 on 2020-08-31 03:58

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advogado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=256, null=True)),
                ('oab', models.CharField(blank=True, max_length=20, null=True)),
                ('cpf', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'advogado',
            },
        ),
        migrations.CreateModel(
            name='Assunto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_assunto', models.IntegerField()),
                ('cod_assunto_pai', models.IntegerField(blank=True, null=True)),
                ('nome', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'assunto',
            },
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_classe', models.IntegerField()),
                ('cod_classe_pai', models.IntegerField(blank=True, null=True)),
                ('nome', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'classe',
            },
        ),
        migrations.CreateModel(
            name='Movimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(blank=True, null=True)),
                ('movimento', models.CharField(blank=True, max_length=250, null=True)),
                ('descricao', models.CharField(blank=True, max_length=1000, null=True)),
                ('sequencia', models.IntegerField(blank=True, null=True)),
                ('movimentado_por', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'movimento',
            },
        ),
        migrations.CreateModel(
            name='MovimentoCnj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_movimento', models.IntegerField()),
                ('cod_movimento_pai', models.IntegerField(blank=True, null=True)),
                ('nome', models.CharField(blank=True, max_length=250, null=True)),
                ('movimento', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'movimentocnj',
            },
        ),
        migrations.CreateModel(
            name='Parte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=256, null=True)),
                ('tipo_documento', models.CharField(blank=True, max_length=40, null=True)),
                ('numero_documento', models.CharField(blank=True, max_length=40, null=True)),
                ('tipo_pessoa', models.CharField(choices=[('Pessoa Física', 'Pessoa Física'), ('Pessoa Jurídica', 'Pessoa Jurídica')], max_length=20)),
                ('polo', models.CharField(choices=[('Parte Ativa', 'Parte Ativa'), ('Parte Passiva', 'Parte Passiva')], max_length=20)),
                ('advogados', models.ManyToManyField(to='base.Advogado')),
            ],
            options={
                'db_table': 'parte',
            },
        ),
        migrations.CreateModel(
            name='Tribunal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orgao', models.CharField(blank=True, max_length=256, null=True)),
                ('instancia', models.CharField(blank=True, max_length=50, null=True)),
                ('sistema', models.CharField(blank=True, max_length=256, null=True)),
                ('estado', models.CharField(blank=True, max_length=2, null=True)),
            ],
            options={
                'db_table': 'tribunal',
            },
        ),
        migrations.CreateModel(
            name='Processo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('client_callback_url', models.CharField(blank=True, max_length=2000, null=True)),
                ('distribuido_em', models.DateTimeField(blank=True, null=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True, null=True)),
                ('juizes', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=120), size=None)),
                ('numero', models.CharField(blank=True, max_length=50, null=True)),
                ('numero_normalizado', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('titulo', models.CharField(blank=True, max_length=500, null=True)),
                ('nivel_de_sigilo', models.CharField(blank=True, max_length=100, null=True)),
                ('valor_da_causa', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('url_tribunal', models.TextField(blank=True, null=True)),
                ('assuntos', models.ManyToManyField(to='base.Assunto')),
                ('classes_processuais', models.ManyToManyField(to='base.Classe')),
                ('movimentos', models.ManyToManyField(to='base.Movimento')),
                ('partes', models.ManyToManyField(to='base.Parte')),
                ('tribunal', models.ForeignKey(blank=True, db_column='tribunal_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tribunal', to='base.Tribunal')),
            ],
            options={
                'db_table': 'processo',
            },
        ),
    ]
