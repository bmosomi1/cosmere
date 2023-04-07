# Generated by Django 2.2.4 on 2022-09-30 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sms', '0001_initial'),
        ('scheduled_sms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulepermonth',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Customer'),
        ),
        migrations.AddField(
            model_name='scheduledmessage',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Customer'),
        ),
    ]