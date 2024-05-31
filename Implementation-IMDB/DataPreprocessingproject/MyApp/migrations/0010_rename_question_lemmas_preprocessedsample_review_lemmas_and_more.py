# Generated by Django 5.0.3 on 2024-04-11 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0009_preprocessedsample_question_stopwords_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preprocessedsample',
            old_name='question_lemmas',
            new_name='review_lemmas',
        ),
        migrations.RenameField(
            model_name='preprocessedsample',
            old_name='question_stopwords',
            new_name='review_stopwords',
        ),
        migrations.RenameField(
            model_name='preprocessedsample',
            old_name='question_tokens',
            new_name='review_tokens',
        ),
        migrations.RenameField(
            model_name='preprocessedsample',
            old_name='sentence_lemmas',
            new_name='sentiment_lemmas',
        ),
        migrations.RenameField(
            model_name='preprocessedsample',
            old_name='sentence_stopwords',
            new_name='sentiment_stopwords',
        ),
        migrations.RenameField(
            model_name='preprocessedsample',
            old_name='sentence_tokens',
            new_name='sentiment_tokens',
        ),
        migrations.RenameField(
            model_name='sample',
            old_name='DocumentID',
            new_name='review',
        ),
        migrations.RenameField(
            model_name='sample',
            old_name='DocumentTitle',
            new_name='sentiment',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='Label',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='Question',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='QuestionID',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='Sentence',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='SentenceID',
        ),
    ]