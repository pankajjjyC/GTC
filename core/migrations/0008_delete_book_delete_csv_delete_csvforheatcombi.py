# Generated by Django 4.0.3 on 2022-06-30 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_csvforheatcombi_alter_csvforheat_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Csv',
        ),
        migrations.DeleteModel(
            name='Csvforheatcombi',
        ),
    ]
