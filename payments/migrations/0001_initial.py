# Generated by Django 3.2 on 2021-04-12 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hierarchy', models.CharField(blank=True, max_length=1024, null=True)),
                ('amount', models.FloatField(null=True)),
                ('type', models.CharField(max_length=128)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.transactions')),
            ],
            options={
                'db_table': 'transactions',
                'managed': True,
            },
        ),
    ]
