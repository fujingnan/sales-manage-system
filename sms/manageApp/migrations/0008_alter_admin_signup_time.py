# Generated by Django 4.1.7 on 2023-07-05 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manageApp", "0007_alter_admin_signup_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="admin",
            name="signup_time",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="注册时间"
            ),
        ),
    ]
