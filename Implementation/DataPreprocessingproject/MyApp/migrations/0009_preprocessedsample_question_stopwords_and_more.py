# Generated by Django 5.0.3 on 2024-04-10 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0008_alter_sample_documentid_alter_sample_documenttitle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='preprocessedsample',
            name='question_stopwords',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='preprocessedsample',
            name='sentence_stopwords',
            field=models.TextField(default=''),
        ),
    ]
