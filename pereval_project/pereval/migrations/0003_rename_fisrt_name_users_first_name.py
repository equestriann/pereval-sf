# Generated by Django 5.0.4 on 2024-04-10 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0002_rename_coord_id_pass_coord_rename_levels_pass_level_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='fisrt_name',
            new_name='first_name',
        ),
    ]