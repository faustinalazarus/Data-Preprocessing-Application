# Generated by Django 5.0.3 on 2024-04-08 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0007_alter_preprocessedsample_original_sample'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='DocumentID',
            field=models.CharField(default='', max_length=20000),
        ),
        migrations.AlterField(
            model_name='sample',
            name='DocumentTitle',
            field=models.CharField(default='', max_length=20000),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Label',
            field=models.CharField(default='', max_length=20000),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Question',
            field=models.CharField(default='', max_length=20000),
        ),
        migrations.AlterField(
            model_name='sample',
            name='QuestionID',
            field=models.CharField(default='', max_length=20000),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Sentence',
            field=models.CharField(default='', max_length=20000),
        ),
        migrations.AlterField(
            model_name='sample',
            name='SentenceID',
            field=models.CharField(default='', max_length=20000),
        ),
    ]
