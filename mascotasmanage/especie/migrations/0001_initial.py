# Generated by Django 4.1.1 on 2022-11-24 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esp', models.IntegerField(max_length=60)),
                ('nombre', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'especie',
            },
        ),
    ]
