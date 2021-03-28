from django.forms import ModelForm
from .models import CreatPoll,OpenPoll

class PollForm(ModelForm):
    
    class Meta:
        model = CreatPoll
        fields = ["Title","o1","o2","o3","o4","on1","on2","on3","on4","one_1","two_1","three_1","four_1"]
    class Meta:
        model = OpenPoll
        fields = ["Title","o1","o2","o3","o4","on1","on2","on3","on4"]



