from .models import Note, Category
from django.forms import ModelForm, Textarea, NumberInput, ModelChoiceField


class NoteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})

    category = ModelChoiceField(queryset=Category.objects.all(), empty_label=None)

    class Meta:
        model = Note

        widgets = {
            'description': Textarea(attrs={'rows': 7, 'cols': 30, 'class': 'form-control'}),
            'date_appoint': NumberInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

        fields = ('title', 'description', 'date_appoint', 'category')


class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Category
        fields = ('name',)

