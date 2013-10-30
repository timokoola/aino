# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from models import ImageFile

from django import forms

class ImageForm(forms.Form):
    imagefile = forms.FileField(
        label='Select an image',
    )


def upload(request):
    # Handle file upload
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = ImageFile(imagefile = request.FILES['imagefile'])
            image.save()

            return HttpResponseRedirect(reverse('frontpage.views.upload'))
    else:
        form = ImageForm()


    return render_to_response(
        'index.html',
        {'form': form},
        context_instance=RequestContext(request)
    )