# Generated by Django 5.0.3 on 2024-03-16 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]
