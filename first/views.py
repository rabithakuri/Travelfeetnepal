from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from .models import Form,Feedback,GalleryImage,Information_slide

# from first import forms
# from first.forms import forminput
# Create your views here.

def index(request):
    testi = Feedback.objects.all().order_by('-id')
    info_slid = Information_slide.objects.all().order_by('-id')
    # testi = Feedback.objects.filter(archived=False).order_by('id') [('-id')]=pixadibata 
    context ={"testi":testi,"info_slid":info_slid}
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

            # send_mail(
            # post.Name + 'from' + post.Country,#subject
            # post.Comment,  #message
            # post.Email,  #from email
            # ['rabidarkers@gmail.com'],#to email -> this is python list ['email','2ndemail'] 'travelfeet.np@gmail.com',
            # )


            return render(request,'first/contact_main.html', {'post_Name': post.Name})
            # return index(request)
            # else:
            #     return index("Fill Valid Information")
        else:
            return render(request,'first/index.html')

        #send an email
        # message_name = request.POST['name']
        # message_email = request.POST['email']
        # message_country = request.POST['country']
        # message_comment = request.POST['message']
        # send_mail(
        #     message_name + 'from' + message_country,#subject
        #     message_comment,  #message
        #     message_email,  #from email
        #     ['travelfeet.np@gmail.com'],#to email -> this is python list ['email','2ndemail']
        # )



def contact(request):
    return render(request, 'first/contact_main.html')

def gallery(request):
    galler = GalleryImage.objects.all().order_by('-id')
    context = {"galler":galler}
    return render(request, 'first/gallery_main.html', context)

def itenary(request):
    return render(request, 'first/itenary_main.html')

def faq(request):
    return render(request, 'first/faq_main.html')

def about(request):
    return render(request, 'first/about_main.html')


# itinary 


def annapurna(request):
    return render(request, 'first/itinaryfiles/annapurna.html')

def langtang(request):
    return render(request, 'first/itinaryfiles/langtang.html')

def annapurnacircuit(request):
    return render(request, 'first/itinaryfiles/annapurnacircuit.html')

def poonhill(request):
    return render(request, 'first/itinaryfiles/poonhill.html')    

def mardihimal(request):
    return render(request, 'first/itinaryfiles/mardihimal.html')   

def everestthreepasses(request):
    return render(request, 'first/itinaryfiles/everestthreepasses.html') 