# Generated by Django 3.2.9 on 2021-12-06 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment_post',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
