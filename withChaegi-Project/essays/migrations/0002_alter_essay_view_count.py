# Generated by Django 4.2 on 2023-07-05 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essays', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essay',
            name='view_count',
            field=models.IntegerField(verbose_name='조회수'),
        ),
    ]
