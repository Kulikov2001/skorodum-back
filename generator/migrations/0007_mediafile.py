# Generated by Django 5.0.2 on 2024-03-06 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0006_question_player_displayed'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=200, unique=True)),
                ('imageUrl', models.FileField(blank=True, db_column='image_url', null=True, upload_to='images/')),
            ],
            options={
                'db_table': 'MediaFile',
                'managed': True,
            },
        ),
    ]
