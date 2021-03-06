# Generated by Django 3.2.2 on 2021-05-15 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210515_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='parent_patronimic',
            field=models.CharField(blank=True, help_text="The student's group can be omitted", max_length=30, null=True, verbose_name="Parent's patronimic"),
        ),
        migrations.AlterField(
            model_name='student',
            name='parent_patronimic',
            field=models.CharField(blank=True, help_text="The student's group can be omitted", max_length=30, null=True, verbose_name="Parent's patronimic"),
        ),
    ]
