# Generated by Django 3.2.7 on 2021-10-06 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_doctor_visit_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='userappointment',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]