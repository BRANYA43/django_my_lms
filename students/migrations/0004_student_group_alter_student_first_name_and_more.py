# Generated by Django 4.1.5 on 2023-02-03 19:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_alter_group_start_date'),
        ('students', '0003_remove_student_age_alter_student_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='groups.group'),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(db_column='f_name', max_length=50, validators=[django.core.validators.MinLengthValidator(3, message='First name field value less then two symbols.')], verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(db_column='l_name', max_length=50, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Last name'),
        ),
    ]
