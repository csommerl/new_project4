from django import forms


class NewPostForm(forms.Form):
    content = forms.CharField(max_length=280, widget=forms.Textarea(attrs={"rows":4, "style": "width: 48rem;", "class": "form-control m-3 mx-auto"}))