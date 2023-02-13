# Generated by Django 4.1.5 on 2023-02-13 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
        ('groups', '0001_initial'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='headman',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='headman_group', to='students.student'),
        ),
        migrations.AddField(
            model_name='group',
            name='teachers',
            field=models.ManyToManyField(blank=True, related_name='groups', to='teachers.teacher'),
        ),
    ]
