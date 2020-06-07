# Generated by Django 2.1.5 on 2020-06-07 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_patientinfo_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinfo',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')], default='Male', max_length=50),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='status',
            field=models.CharField(choices=[('Single', 'Single'), ('Married', 'Married')], default='Single', max_length=20),
        ),
    ]