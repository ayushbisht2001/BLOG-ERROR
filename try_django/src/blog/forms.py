from django import forms
from .models import *
class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)

class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title' ,'image','slug' , 'content' , 'publish_date']
    def clean_title(self,*args,**kwargs):
        instance = self.instance
        title = self.cleaned_data.get("title")
        qs = BlogPost.objects.filter(title__iexact=title) # title__iexact :  it basically ignore the case-sensitivity  ;  title = lower(title)
        if instance is not None:
            qs = qs.exclude(pk = instance.pk)  # same as  (  id = instance.id  )
        if qs.exists():
            raise forms.ValidationError("This title is already been used , pls add another one ")
        return title

