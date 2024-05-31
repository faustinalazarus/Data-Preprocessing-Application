from import_export import resources
from .models import Sample

class SampleResource(resources.ModelResource):
    class Meta: 
        model = Sample
