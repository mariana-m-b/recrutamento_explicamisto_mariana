# Generated by Django 5.0 on 2023-12-27 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_explicamisto', '0018_alter_user_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telephone',
            field=models.IntegerField(),
        ),
    ]
