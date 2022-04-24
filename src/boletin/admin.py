from django.contrib import admin
from .models import Registrado
from .forms import RegModelForm



class AdminRegistrado(admin.ModelAdmin):
	list_display=["email","nombre","timestamp"]
	list_filter= ["timestamp"]
	list_editable=["nombre"]
	search_fields=["email","nombre"]

	#class Meta:
		#model=Registrado



admin.site.register(Registrado,AdminRegistrado)