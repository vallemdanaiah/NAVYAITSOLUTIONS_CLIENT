# Generated by Django 4.2.20 on 2025-03-17 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Solutions', '0002_applyforproject_onlinetraining'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getintouch',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]
