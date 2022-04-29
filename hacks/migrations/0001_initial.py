# Generated by Django 4.0.4 on 2022-04-29 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Persistence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('api', models.ForeignKey(default='None', on_delete=django.db.models.deletion.SET_DEFAULT, to='hacks.api')),
                ('client', models.ForeignKey(default='VanillaJS', on_delete=django.db.models.deletion.SET_DEFAULT, to='hacks.client')),
                ('persistence', models.ForeignKey(default='None', on_delete=django.db.models.deletion.SET_DEFAULT, to='hacks.persistence')),
            ],
        ),
    ]
