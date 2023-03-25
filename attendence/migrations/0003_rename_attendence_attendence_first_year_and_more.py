# Generated by Django 4.1.2 on 2023-02-19 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_alter_course_period_batch'),
        ('accounts', '0002_alter_student_batch'),
        ('attendence', '0002_delete_holidays_alter_attendence_course_period_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='attendence',
            new_name='attendence_first_year',
        ),
        migrations.CreateModel(
            name='attendence_third_year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('course_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course_period')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.student')),
            ],
            options={
                'unique_together': {('user', 'course_period', 'date')},
            },
        ),
        migrations.CreateModel(
            name='attendence_second_year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('course_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course_period')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.student')),
            ],
            options={
                'unique_together': {('user', 'course_period', 'date')},
            },
        ),
        migrations.CreateModel(
            name='attendence_fourth_year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('course_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course_period')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.student')),
            ],
            options={
                'unique_together': {('user', 'course_period', 'date')},
            },
        ),
    ]
