# Generated by Django 3.2.2 on 2021-05-14 22:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='parent_patronimic',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name="Parent's patronimic"),
        ),
        migrations.AlterField(
            model_name='student',
            name='parent_patronimic',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name="Parent's patronimic"),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_group',
            field=models.ForeignKey(blank=True, help_text="The student's group can be omitted", null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.studentgroup'),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(help_text='A student must to be related to a user account', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='studentgroup',
            name='name',
            field=models.CharField(help_text='The name must be unique within one year of studies', max_length=10),
        ),
    ]