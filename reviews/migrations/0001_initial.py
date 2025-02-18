# Generated by Django 4.2.18 on 2025-02-02 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('rating', models.PositiveSmallIntegerField(default=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
