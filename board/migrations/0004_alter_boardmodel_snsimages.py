# Generated by Django 4.1.5 on 2023-01-26 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_alter_boardmodel_good_alter_boardmodel_read_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='snsimages',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
