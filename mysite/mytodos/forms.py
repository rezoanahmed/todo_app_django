from django import forms
from mytodos import models
class add_todo(forms.ModelForm):
    class Meta:
        model = models.todo
        fields = "__all__"