# Generated by Django 2.2.20 on 2021-06-01 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]