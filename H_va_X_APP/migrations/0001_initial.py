# Generated by Django 4.0.4 on 2022-05-09 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Togri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soz', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Natogri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('natogri_soz', models.CharField(max_length=50)),
                ('togri', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='H_va_X_APP.togri')),
            ],
        ),
    ]
