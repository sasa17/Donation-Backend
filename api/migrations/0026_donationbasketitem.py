# Generated by Django 2.2.7 on 2020-04-01 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20200401_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonationBasketItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donationbasket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.DonationBasket')),
                ('item', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.Menu')),
            ],
        ),
    ]
