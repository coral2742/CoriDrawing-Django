# Generated by Django 4.1 on 2023-03-18 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drawings', '0002_drawingcategory_drawingitem_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drawingitem',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drawings.drawingcategory'),
        ),
    ]
