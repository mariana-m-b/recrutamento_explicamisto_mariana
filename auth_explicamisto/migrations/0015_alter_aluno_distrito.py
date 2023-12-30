# Generated by Django 5.0 on 2023-12-27 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_explicamisto', '0014_alter_explicador_ciclo_de_estudos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='distrito',
            field=models.CharField(choices=[('Aveiro', 1), ('Beja', 2), ('Braga', 3), ('Bragança', 4), ('Castelo Branco', 5), ('Coimbra', 6), ('Évora', 7), ('Faro', 8), ('Guarda', 9), ('Leiria', 10), ('Lisboa', 11), ('Portalegre', 12), ('Porto', 13), ('Santarém', 14), ('Setúbal', 15), ('Viana do Castelo', 16), ('Vila Real', 17), ('Viseu', 18), ('Madeira', 19), ('Açores', 20)], default='', max_length=20),
        ),
    ]
