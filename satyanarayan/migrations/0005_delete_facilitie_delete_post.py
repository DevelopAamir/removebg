# Generated by Django 4.1.7 on 2023-07-13 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("satyanarayan", "0004_alter_facilitie_img"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Facilitie",
        ),
        migrations.DeleteModel(
            name="Post",
        ),
    ]
