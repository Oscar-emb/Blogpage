# Generated by Django 4.0.4 on 2022-05-31 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_title', models.CharField(max_length=1000)),
                ('form_content', models.CharField(max_length=10000)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
