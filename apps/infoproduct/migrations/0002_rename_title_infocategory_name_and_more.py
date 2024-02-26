# Generated by Django 4.1.7 on 2024-02-17 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('infoproduct', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infocategory',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='infoproduct',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='infoproduct', to='infoproduct.infocategory', verbose_name='Категория'),
        ),
    ]
