# Generated by Django 5.0 on 2023-12-27 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_explicamisto', '0005_scholar_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholar_info',
            name='year1',
            field=models.CharField(choices=[('10', '10'), ('11', '11'), ('13', '13')], default='', max_length=2),
        ),
    ]
