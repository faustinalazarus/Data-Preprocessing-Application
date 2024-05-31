from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Sample, PreprocessedSample

#register your models here

@admin.register(Sample)
class SampleAdmin(ImportExportModelAdmin):
    list_display = ('QuestionID','Question','DocumentID','DocumentTitle','SentenceID','Sentence','Label')

@admin.register(PreprocessedSample)
class PreprocessedSampleAdmin(ImportExportModelAdmin):
    list_display = ('question_tokens','question_lemmas','sentence_tokens','sentence_lemmas','question_stopwords','sentence_stopwords')