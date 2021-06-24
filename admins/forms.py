from django import forms
from users.forms import UserRegisterForm, UserProfileForm#, UserChangeForm


from users.models import User

class UserAdminRegisterForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields =  ('username', 'email', 'image', 'first_name', 'last_name', 'password1', 'password2')

class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': False}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4', 'readonly': False}))


#class UserAdminProductCategory(UserChangeForm):
    #name = forms.CharField(max_length=64, unique=True)
    #description = models.TextField(blank=True, null=True) # описание может быть или отсутствовать

    # class Meta:
    #     model = User
    #     fields =  ('username', 'email', 'image', 'first_name', 'last_name', 'password1', 'password2')

#  from django.forms import ModelForm
#  from myapp.models import Article
#
#  Create the form class.
#  class ArticleForm(ModelForm):
#      class Meta:
#          model = Article
#          fields = ['pub_date', 'headline', 'content', 'reporter']
#
#  Creating a form to add an article.
#  form = ArticleForm()
#
#  Creating a form to change an existing article.
#  article = Article.objects.get(pk=1)
#  form = ArticleForm(instance=article)