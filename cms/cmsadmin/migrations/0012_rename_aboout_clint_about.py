# Generated by Django 3.2.3 on 2021-06-20 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsadmin', '0011_alter_hr_education'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clint',
            old_name='aboout',
            new_name='about',
        ),
    ]
