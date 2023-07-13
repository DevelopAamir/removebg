import os
from django.http import HttpResponse

from django.shortcuts import render
from PIL import Image
from rembg import remove
from django.views.decorators.csrf import csrf_exempt
from mysite import settings

def index(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['image']
        # Open the uploaded file using PIL's Image module
        input_image = Image.open(uploaded_file)
        # Process the input image using the `remove()` function
        output_image = remove(input_image)
        # Create a response object with the processed image
        response = HttpResponse(content_type='image/png')
        # Save the processed image to the response object
        output_image.save(response, 'PNG')
        # Set the content disposition header to force a download
        response['Content-Disposition'] = 'attachment; filename="output.png"'

        return response
    return render(request, 'index.html',)

@csrf_exempt
def removebg(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['image']

        # Open the uploaded file using PIL's Image module
        input_image = Image.open(uploaded_file)

        # Process the input image using the `remove()` function
        output_image = remove(input_image)

        # Create a response object with the processed image
        response = HttpResponse(content_type='image/png')

        # Save the processed image to the response object
        output_image.save(response, 'PNG', quality=100)

        # Set the content disposition header to force a download
        response['Content-Disposition'] = f'attachment; filename="removedbg-{uploaded_file.name}.png"'

        return response
    return render(request, 'index.html',)