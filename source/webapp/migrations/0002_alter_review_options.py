# Generated by Django 4.0.3 on 2022-03-05 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'permissions': (('delete_own_review', 'Delete own Review'), ('change_own_review', 'Change own Review')), 'verbose_name': 'Review', 'verbose_name_plural': 'Reviews'},
        ),
    ]
