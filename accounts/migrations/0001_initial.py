# Generated by Django 3.0.5 on 2020-09-24 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='student_tymtable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_grp', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='1', max_length=10)),
                ('specialization', models.CharField(default='', max_length=10)),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], default='Monday', max_length=50)),
                ('First_lech', models.CharField(blank=True, max_length=50, null=True)),
                ('sec_lech', models.CharField(blank=True, max_length=50, null=True)),
                ('third_lech', models.CharField(blank=True, max_length=50, null=True)),
                ('fourth_lech', models.CharField(blank=True, max_length=50, null=True)),
                ('fifth_lech', models.CharField(blank=True, max_length=50, null=True)),
                ('sixth_lech', models.CharField(blank=True, max_length=50, null=True)),
                ('sev_lech', models.CharField(blank=True, max_length=50, null=True)),
                ('First_lech_teacher', models.CharField(blank=True, max_length=50, null=True)),
                ('sec_lech_teacher', models.CharField(blank=True, max_length=50, null=True)),
                ('third_lech_teacher', models.CharField(blank=True, max_length=50, null=True)),
                ('fourth_lech_teacher', models.CharField(blank=True, max_length=50, null=True)),
                ('fifth_lech_teacher', models.CharField(blank=True, max_length=50, null=True)),
                ('sixth_lech_teacher', models.CharField(blank=True, max_length=50, null=True)),
                ('sev_lech_teacher', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='teacher_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.CharField(max_length=10)),
                ('rollnumber', models.IntegerField()),
                ('class_Group', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='1', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='teacher_timetable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], default='Monday', max_length=50)),
                ('First_lecture', models.CharField(blank=True, max_length=50, null=True)),
                ('second_lecture', models.CharField(blank=True, max_length=50, null=True)),
                ('third_lecture', models.CharField(blank=True, max_length=50, null=True)),
                ('fourth_lecture', models.CharField(blank=True, max_length=50, null=True)),
                ('fifth_lecture', models.CharField(blank=True, max_length=50, null=True)),
                ('sixth_lecture', models.CharField(blank=True, max_length=50, null=True)),
                ('seventh_lecture', models.CharField(blank=True, max_length=50, null=True)),
                ('First_link', models.CharField(blank=True, max_length=50, null=True)),
                ('second_link', models.CharField(blank=True, max_length=50, null=True)),
                ('third_link', models.CharField(blank=True, max_length=50, null=True)),
                ('fourth_link', models.CharField(blank=True, max_length=50, null=True)),
                ('fifth_link', models.CharField(blank=True, max_length=50, null=True)),
                ('sixth_link', models.CharField(blank=True, max_length=50, null=True)),
                ('seventh_link', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]