# Generated by Django 4.0.2 on 2022-03-02 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_motif_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='motif',
            old_name='motif',
            new_name='libelle_motif',
        ),
    ]