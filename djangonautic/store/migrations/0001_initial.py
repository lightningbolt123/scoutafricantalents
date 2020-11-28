# Generated by Django 3.0.7 on 2020-11-06 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(default=None, upload_to='accountType/icon')),
                ('membership_type', models.CharField(max_length=50)),
                ('account_features', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('time_frame', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membership_type', models.CharField(blank=True, max_length=20)),
                ('price_of_subscription', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('subscriber_first_name', models.CharField(blank=True, max_length=30)),
                ('subscriber_last_name', models.CharField(blank=True, max_length=30)),
                ('subscriber_email', models.CharField(blank=True, max_length=5)),
                ('transaction_fee', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('date_of_transaction', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
