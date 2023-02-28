# Generated by Django 3.2.16 on 2023-02-10 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_remove_profile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('male', 'Мужской'), ('female', 'Женский')], default=None, max_length=16, null=True, verbose_name='Пол пользователя'),
        ),
    ]
