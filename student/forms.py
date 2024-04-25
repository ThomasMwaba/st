from django import forms
from .models import Submit

class SubmitForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your name and surname"}))
    project = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Project Name"}))
    progress = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","placeholder":"What did you do on the project today?"}))
    how = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","placeholder":"How did you use vertical or horizontal learning today?"}))
    class Meta:
        model = Submit
        fields = ['name','grade','project','progress','hours','learning','how']