from django import forms

from .models import ConversationModel, ConversationMessageModel


class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessageModel
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                "class": 'w-full py-4 px-6 rounded-xl border'
            })
        }