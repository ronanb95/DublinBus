# Generated by Django 3.0.3 on 2020-08-06 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_plannedjourney'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favstop',
            name='id',
        ),
        migrations.AlterField(
            model_name='favstop',
            name='stopid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]