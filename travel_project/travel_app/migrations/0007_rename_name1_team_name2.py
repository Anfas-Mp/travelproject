# Generated by Django 4.2.2 on 2023-06-21 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0006_rename_desc1_team_desc2_rename_img1_team_img2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='name1',
            new_name='name2',
        ),
    ]
