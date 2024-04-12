from django import forms
from .models import Submit

class SubmitForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your Name"}))
    project = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Project Name"}))
    progress = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","placeholder":"What did you do today?"}))
    how = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","placeholder":"How did you use the method?"}))
    class Meta:
        model = Submit
        fields = ['name','grade','project','progress','hours','learning','how']
        
        # def __init__(self, *args,**kwargs):
        #     def __init__(self, *args, **kwargs):
        #         super().__init__(*args, **kwargs)
        #         self.fields["name"].widget.attrs.update({"placeholder":"name"})