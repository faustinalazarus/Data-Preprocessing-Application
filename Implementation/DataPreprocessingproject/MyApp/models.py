from django.db import models

class Sample(models.Model):
    QuestionID = models.CharField(max_length=20000, default='')
    Question = models.CharField(max_length=20000, default='')
    DocumentID = models.CharField(max_length=20000, default='')
    DocumentTitle = models.CharField(max_length=20000, default='')
    SentenceID = models.CharField(max_length=20000, default='')
    Sentence = models.CharField(max_length=20000, default='')
    Label = models.CharField(max_length=20000, default='')
    csv_file = models.FileField(upload_to='csv_files/', null=True, blank=True)

class PreprocessedSample(models.Model):
    original_sample = models.ForeignKey('Sample', on_delete=models.CASCADE)
    question_tokens = models.TextField()
    question_lemmas = models.TextField()
    sentence_tokens = models.TextField()
    sentence_lemmas = models.TextField()
    question_stopwords = models.TextField(default='')
    sentence_stopwords = models.TextField(default='')