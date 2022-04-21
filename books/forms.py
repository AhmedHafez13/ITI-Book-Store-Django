from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    publish_date = forms.CharField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Book
        fields = ["author", "title", "publish_date", "price", "appropriate_for", "cover_image"]

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            print(visible.field.widget.input_type)
