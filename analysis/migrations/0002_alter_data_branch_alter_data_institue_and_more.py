# Generated by Django 5.0.6 on 2024-06-03 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("analysis", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="data",
            name="Branch",
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name="data",
            name="Institue",
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name="data",
            name="Quota",
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name="data",
            name="Seat_Type",
            field=models.CharField(max_length=500),
        ),
    ]
