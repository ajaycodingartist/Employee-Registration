from django import forms
# from django.contrib.auth.forms import UserCreationForm
from .models import employer_registration
from .models import employee_registration
from .models import job

class employer_registrationForm(forms.ModelForm):
    GENDER=[('Male','Male'),('Female','Female'),('Others','Others')]
    gender = forms.CharField(label='Gender',widget=forms.RadioSelect(choices=GENDER))
    class Meta:
        model = employer_registration
        fields = '__all__'

class employee_registrationForm(forms.ModelForm):
    GENDER=[('Male','Male'),('Female','Female'),('Others','Others')]
    gender = forms.CharField(label='Gender',widget=forms.RadioSelect(choices=GENDER))
    class Meta:
        model = employee_registration
        fields = '__all__'

class DateInput(forms.DateInput):
    input_type = 'date'

class jobForm(forms.ModelForm):
    workername = forms.CharField(label='Workername', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'on', 'style': 'height: 30px; width: 400px; border: transparent;', 'readonly': True}))
    job_description = forms.CharField(label='Description', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'on', 'style': 'height: 30px; width: 400px; border: transparent;', 'readonly': True}))
    job_location = forms.CharField(label='Location', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'on', 'style': 'height: 30px; width: 400px; border: transparent;', 'readonly': True}))
    class Meta:
        model = job
        fields = ['workername','job_description','job_location','job_date']
        widgets = {
            'job_date': DateInput(),
        }