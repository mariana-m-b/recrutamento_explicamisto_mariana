# Generated by Django 5.0 on 2023-12-25 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_explicamisto', '0002_remove_user_birth_date_remove_user_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telephone1',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]