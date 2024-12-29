# Generated by Django 4.2.5 on 2024-12-29 19:29

import datetime
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
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=9)),
                ('year_of_graduation', models.IntegerField(default=2023)),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': 'Subject',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('Years_Of_Completion', models.IntegerField()),
                ('order_of_completion', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('content', models.TextField()),
                ('excerpt', models.TextField(default='', editable=False, max_length=500)),
                ('slug', models.SlugField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=9)),
                ('current', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('RegistrationNumber', models.CharField(help_text='Registration Number', max_length=9, unique=True)),
                ('picture', models.ImageField(upload_to='student-images')),
                ('firstname', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
                ('middlename', models.CharField(blank=True, max_length=32)),
                ('state_of_origin', models.CharField(max_length=32)),
                ('DateOfBirth', models.DateField(default=datetime.datetime.now)),
                ('Class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.class')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='StudentResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=1)),
                ('term', models.CharField(choices=[('FIRST TERM', 'FIRST TERM'), ('SECOND TERM', 'SECOND TERM'), ('THIRD TERM', 'THIRD TERM')], max_length=32)),
                ('average', models.FloatField(default=100)),
                ('Position', models.IntegerField(default=100)),
                ('RemarkFromTeacher', models.CharField(default='', max_length=100)),
                ('RemarkFromPrincipal', models.CharField(default='', max_length=100)),
                ('section', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.level')),
                ('session', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.session')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result', to='SchoolApp.student')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='school_data')),
                ('Data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='SchoolApp.schooldata')),
            ],
        ),
        migrations.CreateModel(
            name='ResultFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='result_sheets')),
                ('level', models.IntegerField(blank=True, default=1)),
                ('term', models.CharField(choices=[('FIRST TERM', 'FIRST TERM'), ('SECOND TERM', 'SECOND TERM'), ('THIRD TERM', 'THIRD TERM')], default=('FIRST TERM', 'FIRST TERM'), max_length=32)),
                ('Class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result_file', to='SchoolApp.class')),
                ('section', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.level')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.session')),
                ('subject', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='result_file', to='SchoolApp.course')),
                ('teacherInCharge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AssessmentScore', models.IntegerField(default=0)),
                ('ExamScore', models.IntegerField(default=0)),
                ('TotalScore', models.IntegerField(default=0, editable=False)),
                ('Grade', models.CharField(default='', editable=False, max_length=1)),
                ('student_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result', to='SchoolApp.studentresult')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_result', to='SchoolApp.course')),
                ('teacherInCharge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.level'),
        ),
    ]
