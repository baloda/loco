# Generated by Django 3.2 on 2021-04-12 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_alter_transactions_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='parent',
        ),
        migrations.AddField(
            model_name='transactions',
            name='parent_id',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
