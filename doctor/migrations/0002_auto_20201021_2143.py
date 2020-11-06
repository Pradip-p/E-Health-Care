# Generated by Django 2.1.5 on 2020-10-22 04:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorinfo',
            name='department',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctorinfo',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]