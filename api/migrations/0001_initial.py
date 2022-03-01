# Generated by Django 4.0.2 on 2022-02-28 18:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academicien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, verbose_name='Statut du academicien')),
                ('matricule', models.CharField(max_length=120, unique=True)),
                ('nom', models.CharField(max_length=50)),
                ('prenoms', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, default='', null=True, upload_to='photo')),
                ('sommeTotalPaieyer', models.DecimalField(decimal_places=3, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)])),
            ],
            options={
                'verbose_name_plural': 'Academiciens',
            },
        ),
        migrations.CreateModel(
            name='Motif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, verbose_name='Statut du motif')),
                ('libelle', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Payement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('heure', models.TimeField(auto_now_add=True)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0.01), django.core.validators.MaxValueValidator(500)])),
                ('academicien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pay_acad', to='api.academicien')),
                ('motif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pay_motif', to='api.motif')),
            ],
            options={
                'verbose_name_plural': 'Payements',
            },
        ),
        migrations.AddField(
            model_name='motif',
            name='lien',
            field=models.ManyToManyField(blank=True, related_name='paiement', through='api.Payement', to='api.Academicien', verbose_name='Lien'),
        ),
        migrations.AddConstraint(
            model_name='payement',
            constraint=models.UniqueConstraint(fields=('date', 'academicien', 'motif'), name='uniqueKey'),
        ),
    ]