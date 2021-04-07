# Generated by Django 2.2.7 on 2019-11-23 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('DR', 'Descriptions'), ('NA', 'Nature'), ('TH', 'Threshold'), ('PE', 'Personal Experiences'), ('SC', 'School')], default='SC', max_length=2),
        ),
    ]
