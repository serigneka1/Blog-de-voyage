# Generated by Django 4.1.4 on 2023-03-13 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment", name="email", field=models.CharField(max_length=255),
        ),
    ]