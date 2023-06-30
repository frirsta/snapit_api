# Generated by Django 4.2.1 on 2023-06-30 18:03

import cloudinary_storage.storage
import cloudinary_storage.validators
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
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('caption', models.TextField(max_length=250)),
                ('video', models.FileField(storage=cloudinary_storage.storage.VideoMediaCloudinaryStorage(), upload_to='snapit/', validators=[cloudinary_storage.validators.validate_video])),
                ('file', models.ImageField(blank=True, storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='snapit/')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_date'],
            },
        ),
    ]