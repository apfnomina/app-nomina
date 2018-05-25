from django.contrib import admin

# Register your models here.
from main.models import Tabulador, Ispt

class TabuladorAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha_final', 'fecha_inicial', 'nivel', 'zona_economica', 'rango', 'sueldo', 'compensacion')
    list_filter = ('fecha_final',)
    date_hierarchy = 'fecha_final'
    ordering = ('-fecha_final',)
    save_on_top = True
    search_fields = ('nivel',)

class IsptAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha_final', 'fecha_inicial', 'tipo_tabla', 'limite_inferior', 'limite_superior', 'cuota_fija', 'excedente', 'bruto')
    list_filter = ('fecha_final',)
    date_hierarchy = 'fecha_final'
    ordering = ('-fecha_final',)
    save_on_top = True
    search_fields = ('tipo_tabla',)

admin.site.register(Tabulador, TabuladorAdmin)
admin.site.register(Ispt, IsptAdmin)
