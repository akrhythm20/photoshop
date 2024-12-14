# Generated by Django 4.0.1 on 2022-01-30 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hub', '0011_alter_customer_image_alter_photographer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='photographer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
