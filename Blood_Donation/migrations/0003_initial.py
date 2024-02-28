# Generated by Django 5.0.2 on 2024-02-16 07:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Blood_Donation', '0002_remove_request_customer_blood_group_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blood_Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('blood_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blood_Donation.blood_group')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blood_Donation.district')),
            ],
        ),
        migrations.CreateModel(
            name='Request_Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('blood_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blood_Donation.blood_group')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blood_Donation.district')),
            ],
        ),
    ]
