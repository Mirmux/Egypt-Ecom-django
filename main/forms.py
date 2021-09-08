from django import forms
from .models import Comment, OnlineBooking


class ContactForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': ('Your first_name')}
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': ('Your last_name')}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': ('Your e-mail')}
        )
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': ('Your phone number')}
        )
    )
    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': ('Your subject')}
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': ('Your message')}
        )
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'description']


class BookingForm(forms.ModelForm):
    class Meta:
        model = OnlineBooking
        fields = ['name', 'email', 'number', 'children', 'description']

