# Generated by Django 4.2.6 on 2024-01-27 03:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Memento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_date', models.DateField()),
                ('title', models.CharField(max_length=75)),
                ('text', models.CharField(max_length=250)),
                ('img', models.ImageField(default='', upload_to='mementos_files/images')),
                ('audio', models.FileField(default='', upload_to='mementos_files/audios')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]