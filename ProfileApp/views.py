from django.shortcuts import render, HttpResponse

# Create your views here.
def helloworld(request):
    return HttpResponse("<H1>Hello World, This is My First Django Web </H1> "
                        "<H2>I Love Python and Django, It's My Life </H2>")

def firspage(request):
    return render(request, 'firstpage.html')

def secondpage(request):
    return render(request, 'secondpage.html')

def thirdpage(request):
    return render(request, 'thirdpage.html')

def hnypage(request):
    return render(request, 'hnypage.html')

def home(request):
    return render(request, 'home.html')









# ?html----------
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
def hnypdf(request):
    pdfmetrics.registerFont(TTFont('THSarabunNew', 'thsarabunnew-webfont.ttf'))
    pdfmetrics.registerFont(TTFont('THSarabunNew-Bold', 'thsarabunnew_bold-webfont.ttf'))
    pdfmetrics.registerFont(TTFont('THSarabunNew-BoldItalic', 'thsarabunnew_bolditalic-webfont.ttf'))
    pdfmetrics.registerFont(TTFont('THSarabunNew-Italic', 'thsarabunnew_italic-webfont.ttf'))
    template = get_template('hnypdf.html')
    context = {"Name": "I am ReportLab"}
    html = template.render(context)
    response = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
    if not pdf.err:
        return HttpResponse(response.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("Error Rendering PDF", status=400)
