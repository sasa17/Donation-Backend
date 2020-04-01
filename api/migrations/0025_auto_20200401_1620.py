# Generated by Django 2.2.7 on 2020-04-01 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_donationbasket_donationbasketitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationbasket',
            name='item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.Menu'),
        ),
        migrations.AddField(
            model_name='donationbasket',
            name='total_donation',
            field=models.ManyToManyField(to='api.Donation'),
        ),
        migrations.DeleteModel(
            name='DonationBasketItem',
        ),
    ]
