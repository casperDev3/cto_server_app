# Generated by Django 4.2.18 on 2025-02-12 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='title',
            new_name='nickName',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='about',
            field=models.CharField(max_length=255),
        ),
    ]
