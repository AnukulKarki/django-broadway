from django import forms
from crud.models import Classroom
class ClassroomForm(forms.Form):
    name = forms.CharField(max_length=20)

class ClassroomModelForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ["name",]