# Generated by Django 2.2.6 on 2019-10-09 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191009_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lock',
            name='lock_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
