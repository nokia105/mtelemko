# Generated by Django 2.0.1 on 2018-07-18 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
