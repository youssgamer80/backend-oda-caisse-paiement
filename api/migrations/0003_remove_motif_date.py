# Generated by Django 4.0.2 on 2022-03-02 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_academicien_date_alter_motif_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='motif',
            name='date',
        ),
    ]