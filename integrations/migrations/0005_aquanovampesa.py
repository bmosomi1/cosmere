# Generated by Django 2.2.4 on 2023-03-28 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0004_olemaxmpesa'),
    ]

    operations = [
        migrations.CreateModel(
            name='AquaNovaMpesa',
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
    ]