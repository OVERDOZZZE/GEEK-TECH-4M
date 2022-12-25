from django import forms


class ProductCreateForm(forms.Form):
    title = forms.CharField(min_length=8)
    description = forms.CharField(widget=forms.Textarea())
    price = forms.IntegerField()
    rate = forms.FloatField(max_value=10)
    commentable = forms.BooleanField(widget=forms.CheckboxInput(attrs={'checked': False}), label='Разрешить отзывы',)


class CommentCreateForm(forms.Form):
    text = forms.CharField(max_length=255, min_length=4, label='Отзыв')
