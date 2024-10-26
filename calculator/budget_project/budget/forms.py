from django import forms
from .models import budget

class ProjectDetails(forms.ModelForm):
    class Meta:
        model = budget
        fields = [
            'project_name',
            'time_of_completion',
            'require_hosting',
            'project_use',
            'require_it_maintenance'
        ]