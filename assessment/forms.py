import os
import openai
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

    def save(self, user):
        assessment_input = super().save(commit=False)

        # Create a os environment variable OPENAI_API_KEY to store the api key
        openai.api_key = os.getenv("OPENAI_API_KEY")
        msg = f"""
        https://www.truity.com/career-planning/holland-code
        https://www.onetonline.org/explore/interests/{assessment_input.hollandCode1}/{assessment_input.hollandCode2}/{assessment_input.hollandCode3}/
        https://fyi.extension.wisc.edu/teencourthub/files/2014/05/Holland-Code-Assessment.pdf
        Based on the above links and your own calculation which job profile is better for me according to my holland career assessment result which is {assessment_input.hollandCode1}, {assessment_input.hollandCode2} and {assessment_input.hollandCode3}, and my high school marks along with the stream is as follows:
        Stream = {assessment_input.stream}
        {assessment_input.subject_1_name} = {assessment_input.subject_1_marks}
        {assessment_input.subject_2_name} = {assessment_input.subject_2_marks}
        {assessment_input.subject_3_name} = {assessment_input.subject_3_marks}
        {assessment_input.subject_4_name} = {assessment_input.subject_4_marks}
        {assessment_input.subject_5_name} = {assessment_input.subject_5_marks}

        Give me 25 such job profile that are suitable for me and have career growth. Tell me why each job profile is suitable for me. Give the output inside an html div tag.
        """
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": msg}]
        )
        result = completion.choices[0].message.content

        assessment_input.result = result
        assessment_input.user = user
        assessment_input.uuid = uuid.uuid4()
        assessment_input.save()
        return assessment_input
