# Generated by Django 5.0 on 2023-12-27 23:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_explicamisto', '0009_delete_school_info_user_distrito_user_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='distrito',
        ),
        migrations.RemoveField(
            model_name='user',
            name='school',
        ),
        migrations.RemoveField(
            model_name='user',
            name='year',
        ),
        migrations.CreateModel(
            name='School_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(choices=[('10', '10'), ('11', '11'), ('12', '12')], default='', max_length=2)),
                ('school', models.TextField(blank=True, max_length=100)),
                ('distrito', models.CharField(choices=[(1, 'Aveiro'), (2, 'Beja'), (3, 'Braga'), (4, 'Bragança'), (5, 'Castelo Branco'), (6, 'Coimbra'), (7, 'Évora'), (8, 'Faro'), (9, 'Guarda'), (10, 'Leiria'), (11, 'Lisboa'), (12, 'Portalegre'), (13, 'Porto'), (14, 'Santarém'), (15, 'Setúbal'), (16, 'Viana do Castelo'), (17, 'Vila Real'), (18, 'Viseu'), (19, 'Madeira'), (20, 'Açores')], default='', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
