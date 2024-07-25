from django.shortcuts import render
from example_app.models import Member

# Create your views here.
def index(request):
    members = Member.objects.all().values()
    context = {
        'members' : members,
    }
    return render(request, 'first_template.html', context)
    