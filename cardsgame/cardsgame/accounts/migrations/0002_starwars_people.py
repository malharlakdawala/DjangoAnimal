# Generated by Django 3.2.9 on 2021-12-05 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Starwars_people',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('height', models.FloatField()),
                ('mass', models.FloatField()),
                ('homeworld', models.CharField(max_length=50)),
            ],
        ),
    ]
