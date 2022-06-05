# Generated by Django 4.0.4 on 2022-06-05 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Téléphone', 'Téléphone'), ('Télévision', 'Télévision'), ('Ordinateur', 'Ordinateur')], max_length=200),
        ),
        migrations.AlterField(
            model_name='commande',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='commande',
            name='pays',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='commande',
            name='ville',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image_publie'),
        ),
    ]
