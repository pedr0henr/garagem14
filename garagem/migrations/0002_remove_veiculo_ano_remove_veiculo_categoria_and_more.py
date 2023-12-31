# Generated by Django 4.2.4 on 2023-08-25 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
        ('garagem', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veiculo',
            name='ano',
        ),
        migrations.RemoveField(
            model_name='veiculo',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='veiculo',
            name='cor',
        ),
        migrations.RemoveField(
            model_name='veiculo',
            name='marca',
        ),
        migrations.RemoveField(
            model_name='veiculo',
            name='modelo',
        ),
        migrations.RemoveField(
            model_name='veiculo',
            name='preco',
        ),
        migrations.AddField(
            model_name='veiculo',
            name='capa',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='uploader.image'),
        ),
    ]
