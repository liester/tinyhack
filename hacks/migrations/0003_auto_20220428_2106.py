# Generated by Django 3.1.1 on 2022-04-29 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacks', '0002_remove_project_api_remove_project_client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='client',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='persistence',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]