from django import forms
from .models import Recipe


class CreateRecipeForm(forms.ModelForm):
    banner = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'hidden', 'accept': 'image/*', 'id': 'file-input'}),
    )

    title = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full focus:outline-none border-2 border-primary p-2 drop-shadow-md font-text',
            'placeholder': 'e.g: Burgers with fries',
            'id': 'title',
        })
    )

    body = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'w-full focus:outline-none border-2 border-primary p-2 drop-shadow-md font-text resize-none',
            'id': 'body',
            'rows': 5,
        })
    )

    duration = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'w-full focus:outline-none border-2 border-primary p-2 drop-shadow-md font-text',
            'id': 'duration',
        })
    )

    difficulty = forms.ChoiceField(
        required=False,
        choices=Recipe.DIFFICULTY_CHOICES,
        widget=forms.Select(attrs={
            'class': 'w-full focus:outline-none border-2 border-primary p-2 drop-shadow-md font-text h-[43px]',
            'id': 'difficulty',
        })
    )

    categories = forms.MultipleChoiceField(
        required=False,
        choices=Recipe.CATEGORY_CHOICES,
        widget=forms.CheckboxSelectMultiple()
    )

    # Un json field
    ingredients = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'h-0 w-0 p-0 border-0',
        })
    )

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError("This field is required")

        return title

    def clean_body(self):
        body = self.cleaned_data.get('body')
        if not body:
            raise forms.ValidationError("This field is required")

        return body

    def clean_duration(self):
        duration = self.cleaned_data.get('duration')
        if not duration:
            raise forms.ValidationError("This field is required")
        else:
            if not isinstance(duration, int):
                raise forms.ValidationError("This field must be a number")
            else:
                if duration < 0:
                    raise forms.ValidationError(
                        "Enter a positive number")

        return duration

    def clean_categories(self):
        categories = self.cleaned_data.get('categories')
        if not categories:
            raise forms.ValidationError("Select at least one category")

        return categories

    class Meta:
        model = Recipe
        fields = '__all__'
        exclude = ['author', 'likes_count', 'created_at', 'updated_at']