# Generated by Django 4.1.7 on 2023-07-04 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manageApp", "0006_admin_signup_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="admin",
            name="signup_time",
            field=models.DateTimeField(auto_now=True, null=True, verbose_name="注册时间"),
        ),
    ]