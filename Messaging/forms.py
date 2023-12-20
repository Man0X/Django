from django import forms
from .models import Message


class MessageCreationForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']

    def __init__(self, *args, user=None, **kwargs):
        super(MessageCreationForm, self).__init__(*args, **kwargs)
        self.user = user

        self.attrs = (
            {'class': 'Form', 'id': 'MessageCreationForm'})

        self.fields['content'].widget.attrs.update(
            {'class': 'custom-class', 'id': 'content'})
        self.fields['content'].label = ''

    def save(self, commit=True):
        instance = super(MessageCreationForm, self).save(commit=False)
        if self.user:
            instance.created_by = self.user
        if commit:
            instance.save()
        return instance
