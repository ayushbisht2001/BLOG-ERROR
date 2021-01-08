from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

    """

    Manage the content by themselves .i.e email

    """
    def clean_email(self,*args , **kwargs):     # clean_full_name() or clean_content() can be accessed
        email = self.cleaned_data.get('email')
        print(email)
        if email.endswith(".edu"):
            raise forms.ValidationError("This is not a valid email , Pls don't use .edu ")
        return email
