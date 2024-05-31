from django.db import models

class Sample(models.Model):
    review = models.CharField(max_length=20000, default='')
    sentiment = models.CharField(max_length=20000, default='')
    csv_file = models.FileField(upload_to='csv_files/', null=True, blank=True)

class PreprocessedSample(models.Model):
    original_sample = models.ForeignKey('Sample', on_delete=models.CASCADE)
    review_tokens = models.TextField()
    review_lemmas = models.TextField()
    sentiment_tokens = models.TextField()
    sentiment_lemmas = models.TextField()
    review_stopwords = models.TextField(default='')
    sentiment_stopwords = models.TextField(default='')