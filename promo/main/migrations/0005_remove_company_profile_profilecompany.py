# Generated by Django 4.1.5 on 2023-01-23 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_datetime_apartment_date_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='profile',
        ),
        migrations.CreateModel(
            name='ProfileCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.company')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
            ],
        ),
    ]
