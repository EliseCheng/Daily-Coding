from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
import datetime

def  current_datetime(request):
    now = datetime.datetime.now()
    t = get_template("current_datetime.html")
    html = t.render(Context({'current_date':now}))
    return HttpResponse(html)

def cmd_exec(request):
    if request.method == 'POST':
        print request.cmd.value
    return render_to_response("cmd.html", { "result" : "test" })
