# Generated by Django 4.2.3 on 2023-07-14 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookclub', '0006_bookclub_weakday'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookclub',
            old_name='weakday',
            new_name='weekday',
        ),
    ]
