# Generated by Django 3.2.18 on 2023-08-28 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drawings', '0010_auto_20230828_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='drawingcategory',
            name='short_description',
            field=models.TextField(blank=True, max_length=500, verbose_name='Description'),
        ),
    ]
