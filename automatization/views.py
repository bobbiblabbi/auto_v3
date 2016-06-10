# -*- coding: utf-8 -*-
from audioop import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import response
from automatization.models import *
from io import BytesIO
from django.contrib import auth
from reportlab.pdfgen import canvas
import StringIO
from reportlab.lib.pagesizes import letter
from pyPdf import PdfFileWriter, PdfFileReader
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *


def get_pages(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PagesForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return render(request, 'get_page_number.html')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = PagesForm()

    return render(request, 'get_page_number.html', {'form': form})


def document(request, id):
    document = Files.objects.get(id=id)
    return render(request, 'document_page.html', {'document': document})


def create_template(request, id):
    document = Files.objects.get(id=id)
    return render(request, 'create_template_page.html', {'document': document})


def test_page(request):
    person = FIO.objects.all()
    return render(request, 'automatization_page.html', {'person': person})


def template_page(request, id):
    person_template = FIO.objects.get(id=id)
    return render(request, 'template_page.html', {'person_template': person_template})


def delete_user(request, id):
    FIO.objects.get(id=id).delete()
    return redirect('test-page')


@login_required(login_url='/login/')
def save_template(request):
    person = FIO.objects.all()
    return render(request, 'automatization_page.html', {'person': person})


@login_required(login_url='/login/')
def home_page(request):
    user_doc = Files.objects.filter(which_user=request.user)
    return render(request, 'home_page.html', {'user_doc': user_doc})


def file_save(request, id):
    doc_id = Files.objects.get(id=id)
    return render(request, 'home_page.html',{'doc_id}': doc_id})

def save_ready_template(request, id):
    person_print = FIO.objects.get(id=id)
    packet = StringIO.StringIO()
    # create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)
    can.drawString(284, 579, "{} {}".format(person_print.name, person_print.surname))
    can.showPage()
    can.drawString(260, 494, "{} {}".format(person_print.name, person_print.surname))
    can.showPage()
    can.save()
    # move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(file("/Users/danilakimov/Desktop/template1.pdf", "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    page = existing_pdf.getPage(1)
    page.mergePage(new_pdf.getPage(1))
    output.addPage(page)
    # finally, write "output" to a real file
    outputStream = file("/Users/danilakimov/Desktop/readytemplate.pdf", "wb")
    output.write(outputStream)
    outputStream.close()
    return render(request, 'template_page.html', {'person_template': person_print})

def send_email(request, id):
    person_print = FIO.objects.get(id=id)
    # creating email
    subject, from_email, to = u'Письмо', 'bobbiblabbi@gmail.com', person_print.email
    text_content = u"Письмо".format(person_print.name, person_print.surname)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_file('/Users/danilakimov/Desktop/readytemplate.pdf')
    msg.send()
    return render(request, 'template_page.html', {'person_template': person_print})


