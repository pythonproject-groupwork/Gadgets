# Generated by Django 4.1.2 on 2023-01-02 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MYapp', '0002_catdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='productdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('pname', models.CharField(blank=True, max_length=50, null=True)),
                ('pquantity', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile')),
            ],
        ),
    ]
