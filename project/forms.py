from django import forms
from .models import Assignment, Submission, Comments
# from django.contrib.admin import widgets


class Assignmentform(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'types', 'total_marks', 'description', 'files', 'end_date']
'''
        def __init__(self, *args, **kwargs):
            super(Assignmentform, self).__init__(*args, **kwargs)
            for key, field in self.fields.items():
                if isinstance(field.widget, forms.TextInput) or \
                    isinstance(field.widget, forms.Textarea) or \
                    isinstance(field.widget, forms.DateInput) or \
                    isinstance(field.widget, forms.DateTimeField) or \
                    isinstance(field.widget, forms.TimeInput):
                    field.widget.attrs.update({'placeholder': field.label})'''
'''
    def __init__(self, *args, **kwargs):
        super(Assignmentform, self).__init__(*args, **kwargs)
        self.fields['end_date'].widget = widgets.AdminSplitDateTime()'''


class Submissionform(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['file']


class Evaluationform(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['assignment', 'submit_by', 'file', 'marks']
