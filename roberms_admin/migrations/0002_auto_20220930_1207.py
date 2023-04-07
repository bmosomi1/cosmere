# Generated by Django 2.2.4 on 2022-09-30 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sms', '0001_initial'),
        ('roberms_admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='sales_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.SalesPerson'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roberms_admin.Company'),
        ),
    ]
