# Generated by Django 4.0.3 on 2022-06-26 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_csv'),
    ]

    operations = [
        migrations.CreateModel(
            name='App_per_jesse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_1', models.BooleanField(default=False)),
                ('app_2', models.BooleanField(default=False)),
                ('app_3', models.BooleanField(default=False)),
                ('app_4', models.BooleanField(default=False)),
                ('app_5', models.BooleanField(default=False)),
                ('app_6', models.BooleanField(default=False)),
                ('app_7', models.BooleanField(default=False)),
                ('app_8', models.BooleanField(default=False)),
                ('user_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
