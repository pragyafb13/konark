# Generated by Django 4.2.2 on 2023-06-22 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soldier', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PersonalData',
            new_name='soldier_personaldata',
        ),
        migrations.AlterModelTable(
            name='soldier_personaldata',
            table=None,
        ),
    ]
