# Generated by Django 4.2.6 on 2024-01-27 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymemento_app', '0006_alter_userprofile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memento',
            name='text',
            field=models.TextField(max_length=250),
        ),
    ]
