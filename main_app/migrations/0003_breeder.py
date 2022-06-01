# Generated by Django 4.0.4 on 2022-06-01 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_verified_artist_breed_verified_breed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breeder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('breeds', models.CharField(max_length=150)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='breeds', to='main_app.breed')),
            ],
        ),
    ]