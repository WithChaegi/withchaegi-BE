# Generated by Django 4.2.3 on 2023-07-14 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookclub', '0002_bookclub_big_category_bookclub_middle_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookclub',
            name='book_photo',
            field=models.ImageField(blank=True, default='bookclub/dallergut.jfif', upload_to='bookclub/', verbose_name='사진'),
        ),
    ]
