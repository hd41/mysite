from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from .forms import NameForm, ContactForm

# Create your views here.
def index(request):
    return render(request, 'form1/index.html')

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)   #populates as well
        #checking whether is valid
        if form.is_valid():
            # we have to process the data in form.cleaned_data
            return HttpResponseRedirect('/thanks/')
    else:   #for empty for if any other method is called
        form = NameForm()
        return render(request,'form1/name.html',{'form': form})

def mail_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['yoyo@example.com']
            print(subject, message, sender, cc_myself)
            if cc_myself:
                recipients.append(sender)
            send_mail(subject, message, sender, recipients)

            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()
        return render(request, 'form1/name.html',{'form':form})

def thanks(request):
    return render(request,'form1/thanks.html')
