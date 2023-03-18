# Generated by Django 4.1 on 2023-03-18 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drawings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrawingCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Title')),
            ],
        ),
        migrations.AddField(
            model_name='drawingitem',
            name='type',
            field=models.CharField(default='Otros', max_length=200, unique=True, verbose_name='Type'),
            preserve_default=False,
        ),
    ]
