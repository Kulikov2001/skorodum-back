# Generated by Django 5.0.2 on 2024-02-26 12:43

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('theme', models.CharField(max_length=300)),
                ('client', models.CharField(max_length=300)),
                ('date', models.DateField()),
                ('remove_answer', models.PositiveIntegerField(default=0)),
                ('one_for_all', models.PositiveIntegerField(default=0)),
                ('question_bet', models.PositiveIntegerField(default=0)),
                ('all_in', models.PositiveIntegerField(default=0)),
                ('team_bet', models.PositiveIntegerField(default=0)),
                ('skip_emails', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'games',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(max_length=300)),
                ('question_text', models.CharField(max_length=300)),
                ('show_image', models.BooleanField(default=False)),
                ('image_before', models.FileField(blank=True, null=True, upload_to='media_before_question/image/', validators=[django.core.validators.FileExtensionValidator(('png', 'jpg', 'jpeg', 'jpeg200', 'gif', 'tiff', 'bmp', 'webp', 'psd', 'heif', 'svg', 'pdf', 'eps', 'ai', 'cdr', 'wmf', 'eme'))])),
                ('image_after', models.FileField(blank=True, null=True, upload_to='media_after_question/image/', validators=[django.core.validators.FileExtensionValidator(('png', 'jpg', 'jpeg', 'jpeg200', 'gif', 'tiff', 'bmp', 'webp', 'psd', 'heif', 'svg', 'pdf', 'eps', 'ai', 'cdr', 'wmf', 'eme'))])),
                ('video_before', models.FileField(blank=True, null=True, upload_to='media_before_question/video', validators=[django.core.validators.FileExtensionValidator(('png', 'jpg', 'jpeg', 'jpeg200', 'gif', 'tiff', 'bmp', 'webp', 'psd', 'heif', 'svg', 'pdf', 'eps', 'ai', 'cdr', 'wmf', 'eme'))])),
                ('video_after', models.FileField(blank=True, null=True, upload_to='media_after_question/video', validators=[django.core.validators.FileExtensionValidator(('png', 'jpg', 'jpeg', 'jpeg200', 'gif', 'tiff', 'bmp', 'webp', 'psd', 'heif', 'svg', 'pdf', 'eps', 'ai', 'cdr', 'wmf', 'eme'))])),
                ('category', models.ManyToManyField(to='generator.category')),
            ],
            options={
                'db_table': 'questions',
            },
        ),
        # migrations.CreateModel(
        #     name='AnswerOptions',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('answer', models.TextField()),
        #         ('answer_is_correct', models.BooleanField(default=False)),
        #         ('quest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generator.question')),
        #     ],
        #     options={
        #         'db_table': 'answer_options',
        #     },
        # ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_type', models.CharField(max_length=300)),
                ('is_test', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=300)),
                ('display_name', models.BooleanField(default=False)),
                ('time_to_answer', models.PositiveIntegerField(default=0)),
                ('use_special_tactics', models.BooleanField(default=False)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generator.game')),
            ],
            options={
                'db_table': 'rounds',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='round_id',
            field=models.ManyToManyField(blank=True, to='generator.round'),
        ),
    ]
