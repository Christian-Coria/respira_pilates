# Generated by Django 3.2 on 2024-03-16 23:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, default='defecto/defecto.png', null=True, upload_to='avatar/%Y/%m/%d')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('domicilio', models.CharField(blank=True, max_length=80)),
                ('telefono', models.CharField(blank=True, max_length=30)),
                ('celular', models.CharField(blank=True, max_length=30)),
                ('documento', models.CharField(blank=True, max_length=30)),
                ('cuit', models.CharField(blank=True, max_length=30)),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]