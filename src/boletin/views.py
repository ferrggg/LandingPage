from django.shortcuts import render

from .forms import ContactForm,RegModelForm

from .models import Registrado

from django.conf import settings
from django.core.mail import send_mail

def inicio(request):
	titulo = "HOLA"
	if request.user.is_authenticated:
		titulo = "Bienvenido %s" %(request.user)
	form =  RegModelForm(request.POST or None)
	context = {
	"titulo": titulo,
	"el_form": form,
	}

	if form.is_valid():
		instance = form.save(commit=False)
		nombre = form.cleaned_data.get("nombre")
		email = form.cleaned_data.get("email")
		if not instance.nombre:
			instance.nombre = "Persona"
		instance.save()

		context = {
		"titulo" : "Gracias %s!" %(nombre)
		}
		if not nombre:
			context = {
			"titulo" : "Gracias %s" %(email)
			}
		# form_data = form.cleaned_data
		# abc = form_data.get("email")
		# abc2 = form_data.get("nombre")
		# obj = Registrado.objects.create(email=abc, nombre=abc2)
	return render(request,"inicio.html",context)
def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_mensaje = form.cleaned_data.get("mensaje")
		form_nombre= form.cleaned_data.get("nombre")
		asunto = 'Forma de Contact'
		email_from = settings.EMAIL_HOST_USER
		email_to = [email_from, "otroemail@gmail.com"]
		email_mensaje = "%s : %s enviado por %s" %(form_nombre, form_mensaje , form_email)
		send_mail(asunto,email_mensaje,email_from,email_to,fail_silenty=False)
		# for key,value in form.cleaned_data.items():
		# 	print (key , value)
	context = {
	"form" : form,
	}
	return render(request, "forms.html",context)
