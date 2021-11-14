# Generated by Django 2.1.15 on 2020-08-19 01:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Multiple_Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, default='option', max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(blank=True, default='', max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='untitled', max_length=200, null=True)),
                ('description', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('color', models.CharField(blank=True, default='#FFCDD2', max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Survey_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_type', models.CharField(max_length=200)),
                ('content', models.CharField(blank=True, default='unknown', max_length=500, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='survey',
            name='questions',
            field=models.ManyToManyField(related_name='surveyss', to='surveys.Survey_Question'),
        ),
        migrations.AddField(
            model_name='survey',
            name='students',
            field=models.ManyToManyField(related_name='surveys', to='accounts.Student'),
        ),
        migrations.AddField(
            model_name='survey',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='student_answer',
            name='q_pk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.Survey_Question'),
        ),
        migrations.AddField(
            model_name='student_answer',
            name='s_pk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.Survey'),
        ),
        migrations.AddField(
            model_name='student_answer',
            name='st_pk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Student'),
        ),
        migrations.AddField(
            model_name='multiple_answer',
            name='q_pk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.Survey_Question'),
        ),
        migrations.AddField(
            model_name='multiple_answer',
            name='s_pk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.Survey'),
        ),
    ]