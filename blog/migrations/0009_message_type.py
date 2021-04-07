# Generated by Django 2.2.7 on 2020-04-19 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200325_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='type',
            field=models.CharField(choices=[('AL', 'Alert'), ('IF', 'Information')], default='IF', max_length=2),
        ),
    ]
