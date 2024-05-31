# views.py
import json
import csv
import io
import spacy
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Sample, PreprocessedSample
from tablib import Dataset
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

# Load the English language model for spaCy
nlp = spacy.load('en_core_web_sm')

# Initialize NLTK's English stop words list
stop_words = set(stopwords.words('english'))

def remove_stopwords(lemmatized_tokens):
    """
    Remove stop words from lemmatized tokens.
    """
    return [token for token in lemmatized_tokens if token not in stop_words]

def tokenize_and_lemmatize(text):
    """
    Tokenize and lemmatize the input text using spaCy.
    """
    doc = nlp(text)
    tokens = [token.text for token in doc]
    lemmatized_tokens = [token.lemma_ for token in doc]
    return tokens, lemmatized_tokens

def tokenize_samples(sample):
    """
    Tokenize the given sample and save it in the PreprocessedSample model.
    """
    review_tokens, _ = tokenize_and_lemmatize(sample.review)
    sentiment_tokens, _ = tokenize_and_lemmatize(sample.sentiment)
    
    processed_sample = PreprocessedSample(
        original_sample=sample,
        review_tokens=review_tokens,
        sentiment_tokens=sentiment_tokens
    )
    processed_sample.save()

def lemmatize_samples(sample):
    """
    Lemmatize the given sample and save it in the PreprocessedSample model.
    """
    _, review_lemmas = tokenize_and_lemmatize(sample.review)
    _, sentiment_lemmas = tokenize_and_lemmatize(sample.sentiment)
    
    processed_sample = PreprocessedSample.objects.filter(original_sample_id=sample.id).first()
    if processed_sample:
        processed_sample.review_lemmas = review_lemmas
        processed_sample.sentiment_lemmas = sentiment_lemmas
        processed_sample.save()

def process_sample(sample, selected_tasks):
    """
    Process the given sample based on the selected tasks.
    """
    review_tokens, review_lemmas = None, None
    sentiment_tokens, sentiment_lemmas = None, None

    if 'tokenization' in selected_tasks:
        review_tokens, _ = tokenize_and_lemmatize(sample.review)
        sentiment_tokens, _ = tokenize_and_lemmatize(sample.sentiment)

    if 'lemmatization' in selected_tasks:
        _, review_lemmas = tokenize_and_lemmatize(sample.review)
        _, sentiment_lemmas = tokenize_and_lemmatize(sample.sentiment)

    if 'stopword_removal' in selected_tasks:
        review_stopwords = remove_stopwords(review_lemmas)
        sentiment_stopwords = remove_stopwords(sentiment_lemmas)

    # Create a single PreprocessedSample object containing the results of all tasks
    processed_sample = PreprocessedSample(
        original_sample=sample,
        review_tokens=review_tokens,
        review_lemmas=review_lemmas,
        sentiment_tokens=sentiment_tokens,
        sentiment_lemmas=sentiment_lemmas,
        review_stopwords=review_stopwords,
        sentiment_stopwords=sentiment_stopwords
    )
    processed_sample.save()

def remove_stopwords_from_samples(sample):
    """
    Remove stop words from lemmatized tokens in the given sample and save it in the PreprocessedSample model.
    """
    _, review_lemmas = tokenize_and_lemmatize(sample.review)
    _, sentiment_lemmas = tokenize_and_lemmatize(sample.sentiment)
    
    # Remove stop words
    review_lemmas = remove_stopwords(review_lemmas)
    sentiment_lemmas = remove_stopwords(sentiment_lemmas)
    
    processed_sample = PreprocessedSample.objects.filter(original_sample_id=sample.id).first()
    if processed_sample:
        processed_sample.review_stopwords = review_lemmas
        processed_sample.sentiment_stopwords = sentiment_lemmas
        processed_sample.save()

def preprocess_samples(selected_tasks):
    """
    Preprocess samples based on selected tasks.
    """
    # Get all samples from the Sample model
    samples = Sample.objects.all()

    # Process each sample based on selected tasks
    for sample in samples:
        # Process the sample for each selected task
        for task in selected_tasks:
            if task == 'tokenization':
                tokenize_samples(sample)
            elif task == 'lemmatization':
                lemmatize_samples(sample)
            elif task == 'stopword_removal':
                remove_stopwords_from_samples(sample)


@csrf_exempt
def run_tasks(request):
    """
    Handle the request to run tasks.
    """
    if request.method == 'POST':
        if not Sample.objects.exists():
            return JsonResponse({'error': 'No CSV file uploaded. Please upload a CSV file first.'})
        data = json.loads(request.body)
        selected_tasks = data.get('tasks', [])
        
        preprocess_samples(selected_tasks)
        
        return JsonResponse({'message': 'Tasks completed successfully.'})
    else:
        return JsonResponse({'error': 'Invalid request method.'})

def upload(request):
    if request.method == 'POST':
        new_sample = request.FILES.get('myfile')

        if not new_sample:
            messages.error(request, 'No file uploaded. Please upload a CSV file first.')
            return render(request, 'home.html')

        if not new_sample.name.endswith('csv'):
            messages.error(request, 'Please upload a CSV file only.')
            return render(request, 'home.html')

        try:
            Sample.objects.all().delete()
            data_set = new_sample.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)  # Skip header row
            for column in csv.reader(io_string):
                Sample.objects.update_or_create(
                    review=column[0],
                    sentiment=column[1]
                )
            messages.success(request, 'File successfully uploaded')
        except Exception as e:
            messages.error(request, f'Error occurred: {str(e)}')
    return render(request, 'home.html')

def download_preprocessed_dataset(request):
    # Retrieve preprocessed samples
    preprocess_samples = PreprocessedSample.objects.all()

    # Create a CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="preprocessed_dataset.csv"'

    # Write CSV headers
    writer = csv.writer(response)
    writer.writerow(['Review Tokens', 'Review Lemmas', 'Review Stopwords', 'Sentiment Tokens', 'Sentiment Lemmas', 'Sentiment Stopwords'])

    # Write preprocessed data to CSV
    for sample in preprocess_samples:
        writer.writerow([
            sample.review_tokens,
            sample.review_lemmas,
            sample.review_stopwords,  # Include stopword-removed lemmatized tokens
            sample.sentiment_tokens,
            sample.sentiment_lemmas,
            sample.sentiment_stopwords  # Include stopword-removed lemmatized tokens
        ])

    return response

def preview(request):
    # Retrieve preprocessed samples
    preprocess_samples = PreprocessedSample.objects.all()[:10]  # Fetch only the first 10 samples

    # Prepare data for rendering in the template
    data = []
    for sample in preprocess_samples:
        data.append({
            'review_tokens': sample.review_tokens,
            'review_lemmas': sample.review_lemmas,
            'review_stopwords': sample.review_stopwords,  # Include stopword-removed lemmatized tokens
            'sentiment_tokens': sample.sentiment_tokens,
            'sentiment_lemmas': sample.sentiment_lemmas,
            'sentiment_stopwords': sample.sentiment_stopwords  # Include stopword-removed lemmatized tokens
        })

    # Render the template with the preprocessed dataset preview
    return render(request, 'home.html', {'preprocessed_data': data})
