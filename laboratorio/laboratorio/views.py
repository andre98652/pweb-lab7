from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from laboratorio.utils import render_to_pdf #created in step 4

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf/invoice.html')
        context ={
            "invoice_id" : 123,
            "customer_name" : "Andre DElgado",
            "amount" : 1399.99,
            "today" : "hoy",
        }
        html = template.render(context)
        pdf = render_to_pdf('pdf/invoice.html',context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("123411231")
            content = "inLine; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
