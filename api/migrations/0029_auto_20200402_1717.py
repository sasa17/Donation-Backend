# Generated by Django 2.2.10 on 2020-04-02 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_auto_20200402_1429'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donationbasket',
            old_name='user',
            new_name='restaurant',
        ),
        migrations.RemoveField(
            model_name='donationbasket',
            name='active',
        ),
        migrations.AddField(
            model_name='donationbasket',
            name='single_restaurant_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
