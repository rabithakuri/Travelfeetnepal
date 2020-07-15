from django.shortcuts import render
from django.contrib import messages
from .models import Form,Feedback

# from first import forms
# from first.forms import forminput
# Create your views here.

def index(request):
    testi = Feedback.objects.all()
    # testi = Feedback.objects.filter(archived=False).order_by('id') [('-id')]=pixadibata 
    context ={"testi":testi}
    return render(request, 'first/index.html', context)

def users(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email'):
            post=Form()

            post.Name = request.POST.get('name')
            post.Email = request.POST.get('email')
            post.Country = request.POST.get('country')
            post.Comment = request.POST.get('message')

            post.save()

            return index(request)
            # else:
            #     return index("Fill Valid Information")
        else:
            return render(request,'first/index.html')

def contact(request):
    return render(request, 'first/contact_main.html')

def gallery(request):
    return render(request, 'first/gallery_main.html')

def itenary(request):
    return render(request, 'first/itenary_main.html')

def faq(request):
    return render(request, 'first/faq_main.html')

def about(request):
    return render(request, 'first/about_main.html')