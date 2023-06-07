# Generated by Django 4.2.2 on 2023-06-07 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('productid', models.IntegerField(primary_key=True, serialize=False)),
                ('productname', models.CharField(max_length=10)),
                ('productcost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('productmfdt', models.DateField()),
                ('productexpdt', models.DateField()),
            ],
        ),
    ]
