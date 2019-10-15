# Generated by Django 2.2.6 on 2019-10-09 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lock',
            fields=[
                ('lock_id', models.AutoField(primary_key=True, serialize=False)),
                ('lock_status', models.BooleanField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='lock',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Lock'),
        ),
    ]
