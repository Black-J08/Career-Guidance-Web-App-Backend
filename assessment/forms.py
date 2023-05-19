import uuid
from django import forms
from .models import Assessment


class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['name', 'age', 'sex', 'stream',
                  'subject_1_name', 'subject_1_marks',
                  'subject_2_name', 'subject_2_marks',
                  'subject_3_name', 'subject_3_marks',
                  'subject_4_name', 'subject_4_marks',
                  'subject_5_name', 'subject_5_marks',
                  'hollandCode1', 'hollandCode2', 'hollandCode3']

    def save(self, user,):
        assessment_input = super().save(commit=False)
        assessment_input.user = user
        assessment_input.uuid = uuid.uuid4()
        assessment_input.save()
        return assessment_input
