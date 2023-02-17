from django.forms import ModelForm,TextInput
from .models import TodoModel
class TodoForm(ModelForm):
    
    class Meta:
        model = TodoModel
        fields = ["title","completed",]
        widgets = {'title':TextInput(attrs={'class':'input','placeholder':'Enter Task'})}