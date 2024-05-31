# Generated by Django 5.0.3 on 2024-04-08 16:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0005_sample_csv_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreprocessedSample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_tokens', models.TextField()),
                ('question_lemmas', models.TextField()),
                ('sentence_tokens', models.TextField()),
                ('sentence_lemmas', models.TextField()),
                ('original_sample', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='MyApp.sample')),
            ],
        ),
    ]