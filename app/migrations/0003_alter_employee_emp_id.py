# Generated by Django 5.0.6 on 2024-06-06 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_depatment_employee_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.IntegerField(),
        ),
    ]
