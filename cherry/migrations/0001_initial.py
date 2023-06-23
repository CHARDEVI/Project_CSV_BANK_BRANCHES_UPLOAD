# Generated by Django 4.2.2 on 2023-06-18 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('IFSC', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('BRANCH', models.CharField(max_length=29)),
                ('ADDRESS', models.TextField()),
                ('CONTACT', models.IntegerField()),
                ('CITY', models.CharField(max_length=22)),
                ('DISTRICT', models.CharField(max_length=29)),
                ('STATE', models.CharField(max_length=29)),
                ('BName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cherry.bank')),
            ],
        ),
    ]
