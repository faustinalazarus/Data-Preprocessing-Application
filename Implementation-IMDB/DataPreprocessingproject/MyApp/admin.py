# admin.py
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Sample, PreprocessedSample

@admin.register(Sample)
class SampleAdmin(ImportExportModelAdmin):
    list_display = ('review', 'sentiment')

@admin.register(PreprocessedSample)
class PreprocessedSampleAdmin(ImportExportModelAdmin):
    list_display = ('review_tokens', 'review_lemmas', 'sentiment_tokens', 'sentiment_lemmas', 'review_stopwords', 'sentiment_stopwords')