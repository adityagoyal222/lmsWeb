# Generated by Django 3.1.3 on 2021-03-12 13:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0004_auto_20210309_1927'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_name', models.CharField(max_length=200)),
                ('assignment_description', models.TextField()),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('due_date', models.DateTimeField(blank=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='SubmitAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200)),
                ('submission_text', models.TextField()),
                ('submission_file', models.FileField(upload_to='')),
                ('submitted_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('graded', models.BooleanField(default=False)),
                ('grade', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('assignment_ques', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='assignments.assignment')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
