# Generated by Django 3.2.9 on 2021-12-06 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_auto_20211205_2304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cards', models.ManyToManyField(to='accounts.Starwars_people')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_status', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('card_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards_details', to='game.deck')),
                ('cards_receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards_receiver', to='game.deck')),
                ('cards_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards_sender', to='game.deck')),
            ],
        ),
    ]
