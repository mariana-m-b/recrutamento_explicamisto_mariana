# Generated by Django 5.0 on 2023-12-27 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_explicamisto', '0016_alter_aluno_distrito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='distrito',
            field=models.CharField(choices=[('Aveiro', 'Aveiro'), ('Beja', 'Beja'), ('Braga', 'Braga'), ('Bragança', 'Bragança'), ('Castelo Branco', 'Castelo Branco'), ('Coimbra', 'Coimbra'), ('Évora', 'Évora'), ('Faro', 'Faro'), ('Guarda', 'Guarda'), ('Leiria', 'Leiria'), ('Lisboa', 'Lisboa'), ('Portalegre', 'Portalegre'), ('Porto', 'Porto'), ('Santarém', 'Santarém'), ('Setúbal', 'Setúbal'), ('Viana do Castelo', 'Viana do Castelo'), ('Vila Real', 'Vila Real'), ('Viseu', 'Viseu'), ('Madeira', 'Madeira'), ('Açores', 'Açores')], default='', max_length=20),
        ),
    ]
