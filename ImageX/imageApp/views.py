from django.shortcuts import render, HttpResponse
from PIL import Image, ImageDraw, ImageFilter
from PIL import ImageFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import FileResponse
from io import BytesIO
import uuid

# Create your views here.
def home(request):
    return render(request, 'app.html')

def data(request):
    
    
    
    image_path = staticfiles_storage.path('images/image-py.jpg')
    image1 = Image.open(image_path)

    #write

    draw = ImageDraw.Draw(image1)

    # one
    font1 = staticfiles_storage.path('fonts/ARLRDBD_0.TTF')
    font = ImageFont.truetype(font1, 18)
    draw.text((200, 251), request.POST.get('facnum'),(0,0,0), font=font)

    #two
    data = request.POST.get('reference')
    data = data.split('*')
    line2 = 330
    for line in data:    
        font2 = staticfiles_storage.path('fonts/ARLRDBD_0.TTF')
        font = ImageFont.truetype(font2, 18)
        draw.text((50, line2), line,(0,0,0), font=font)
        line2+=20
    
    string = request.POST.get('designation')
    # Split the input text into lines
    lines = string.strip().split('*')
    line1 = 570

    for line in lines:
    # Split the line into parts
        parts = line.split('-')

        #three
        font3 = staticfiles_storage.path('fonts/Athelas-Bold.ttf')
        #font = ImageFont.truetype(font3, 21)

        #font3 = staticfiles_storage.path('fonts/ARIALBD 1.ttf')
        font = ImageFont.truetype(font3, 18)
        draw.text((50, line1),'- '+ parts[0],(0,0,0), font=font)
        font4 = staticfiles_storage.path('fonts/ARIALBD 1.TTF')
        font = ImageFont.truetype(font4, 18)
        draw.text((760, line1), parts[1],(0,0,0), font=font)
        line1 += 30


 

    #five
    font5 = staticfiles_storage.path('fonts/ARLRDBD_0.TTF')
    font = ImageFont.truetype(font5, 18)
    draw.text((90, 1005), request.POST.get('price'),(0,0,0), font=font)

    #six
    font6 = staticfiles_storage.path('fonts/ARLRDBD_0.TTF')
    font = ImageFont.truetype(font6, 18)
    draw.text((280, 1005), request.POST.get('vat'),(0,0,0), font=font)

    #seven
    font7 = staticfiles_storage.path('fonts/ARLRDBD_0.TTF')
    font = ImageFont.truetype(font7, 18)
    draw.text((410, 1005), request.POST.get('price'),(0,0,0), font=font)

    #eight
    font8 = staticfiles_storage.path('fonts/ArialCEMTBlack.ttf')
    font = ImageFont.truetype(font8, 21)
    draw.text((570, 250), request.POST.get('egy'),(0,0,0), font=font)

    #nine
    egy_data = request.POST.get('egy2')
    egy_data = egy_data.split('*')
    line4 = 277
    
    for egy in egy_data:
        font9 = staticfiles_storage.path('fonts/ARIALBD.TTF')
        font = ImageFont.truetype(font9, 21)
        draw.text((570, line4), egy,(0,0,0), font=font)
        line4 += 20
   

    #ten
    font10 = staticfiles_storage.path('fonts/ARIALBD.TTF')
    font = ImageFont.truetype(font10, 18)
    draw.text((623, 363), request.POST.get('date'),(0,0,0), font=font)

    #image1 = image1.copy()
    #image1.putalpha(200)

    image1 = image1.convert("RGB")

    image1.save(staticfiles_storage.path('images/final_image/'+uuid.uuid4().hex +'.jpg'), quality=95)
    
    
    # Convert image to RGB
    image = image1.convert("RGB")
    
    # Save image to a BytesIO object
    img_io = BytesIO()
    image1.save(img_io, format='JPEG', quality=95)
    img_io.seek(0)
    
    # Return the image as an HTTP response
    response = HttpResponse(img_io, content_type='image/jpeg')
    response['Content-Disposition'] = 'attachment; filename="final-image.jpg"'
    return response
    
