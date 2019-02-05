# Generated by Django 2.1.5 on 2019-02-04 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Integration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=100)),
                ('secret', models.CharField(max_length=64)),
                ('oauth_token', models.CharField(max_length=100)),
                ('bot_username', models.CharField(max_length=32)),
                ('server_url', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'integration',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mr_matcher', models.CharField(blank=True, max_length=150)),
                ('mr_failed_content', models.CharField(blank=True, max_length=150)),
                ('mr_accepted_content', models.CharField(blank=True, max_length=150)),
                ('mr_default_assignee', models.CharField(blank=True, max_length=150)),
                ('integration', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Integration')),
            ],
            options={
                'db_table': 'preferences',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, unique=True)),
                ('password', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.AddField(
            model_name='integration',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
    ]