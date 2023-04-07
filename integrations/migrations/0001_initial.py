# Generated by Django 2.2.4 on 2022-09-30 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiwamaMpesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=250)),
                ('amount', models.CharField(max_length=250)),
                ('reference', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=250)),
                ('account_number', models.IntegerField(null=True)),
                ('organization_balance', models.CharField(max_length=250, null=True)),
                ('is_processed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Miwama Mpesa',
                'verbose_name_plural': 'Miwama Mpesa',
            },
        ),
        migrations.CreateModel(
            name='NopeMpesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('phone_number', models.CharField(max_length=250)),
                ('amount', models.CharField(max_length=250)),
                ('reference', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=250)),
                ('account_number', models.IntegerField(null=True)),
                ('till_number', models.IntegerField(null=True)),
                ('processed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(null=True)),
                ('organization_balance', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PerezuMpesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('phone_number', models.CharField(max_length=250)),
                ('amount', models.CharField(max_length=250)),
                ('reference', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=250)),
                ('account_number', models.IntegerField(null=True)),
                ('till_number', models.IntegerField(null=True)),
                ('processed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(null=True)),
                ('organization_balance', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RealBoutiqueMpesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=250)),
                ('amount', models.CharField(max_length=250)),
                ('reference', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=250)),
                ('account_number', models.IntegerField(null=True)),
                ('organization_balance', models.CharField(max_length=250, null=True)),
                ('is_processed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Real Boutique M-pesa Record',
                'verbose_name_plural': 'Real Boutique M-pesa Records',
            },
        ),
    ]
