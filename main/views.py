from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection

# Create your views here.
def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc],row))
        for row in cursor.fetchall()
    ]

def home(request):
    return HttpResponseRedirect('/admin/main')

class RangoIsptViewSet(APIView):

    def get(self, request, *args, **kw):
        cursor = connection.cursor()
        valorFin = kw['fec_fin']
        cantidad = kw['monto']

        query = '''
				select %s as cantidad_mensual, limite_inferior, limite_superior, excedente, cuota_fija
                from main_ispt
                where fecha_final = '%s'
                and tipo_tabla = '80'
                and limite_inferior <= %s
                and limite_superior >= %s
                order by id
        ''' % (cantidad, valorFin, cantidad, cantidad)
        cursor.execute(query)
        totales_list = dictfetchall(cursor)
        response = Response(totales_list, status=status.HTTP_200_OK)
        return response

class CalculoIsptViewSet(APIView):

    def get(self, request, *args, **kw):
        cursor = connection.cursor()
        valorFin = kw['fec_fin']
        cantidad = kw['monto']

        query = '''
				select %s as cantidad_mensual,
                      (%s - limite_inferior) * excedente /100 + cuota_fija as ispt_mensual
                from main_ispt
                where fecha_final = '%s'
                and tipo_tabla = '80'
                and limite_inferior <= %s
                and limite_superior >= %s
                order by id
        ''' % (cantidad, cantidad, valorFin, cantidad, cantidad)
        cursor.execute(query)
        totales_list = dictfetchall(cursor)
        response = Response(totales_list, status=status.HTTP_200_OK)
        return response

class SueldoPorNivelViewSet(APIView):

    def get(self, request, *args, **kw):
        cursor = connection.cursor()
        valorFin = kw['fec_fin']
        nivel = kw['nivel']

        query = '''
            select nivel, zona_economica, rango, sueldo, compensacion
            from main_tabulador
            where fecha_final = '%s'
            and nivel like '%s%%'
            order by 1,2,3
        ''' % (valorFin, nivel.upper())
        print(query)
        cursor.execute(query)
        totales_list = dictfetchall(cursor)
        response = Response(totales_list, status=status.HTTP_200_OK)
        return response
