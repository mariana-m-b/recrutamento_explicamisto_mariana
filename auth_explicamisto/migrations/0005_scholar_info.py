# Generated by Django 5.0 on 2023-12-27 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_explicamisto', '0004_remove_user_telephone1_user_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='scholar_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year1', models.CharField(choices=[('10', '10'), ('11', '11'), ('12', '12')], default='', max_length=2)),
            ],
        ),
    ]
