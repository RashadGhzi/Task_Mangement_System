from .models import Task
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'photos', 'due_date', 'priority', 'is_complete', 'user']
        widgets = {
            'title':forms.TextInput(attrs={"class":"form-control"}, ),
            'description':forms.Textarea(attrs={"class":"form-control", "rows":5}),
            'photos':forms.ClearableFileInput(attrs={"class":"task-img"}),
            'priority':forms.Select(attrs={"class":"form-select"}),
            'is_complete':forms.CheckboxInput(attrs={"class":"form-check-input"}),
            'user': forms.Select(attrs={"class":"form-select"}),
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['photos'].widget.attrs['accept'] = 'image/*'  # Allow only image files
        self.fields['photos'].required = False
        self.fields['is_complete'].required = False