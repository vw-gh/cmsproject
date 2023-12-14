from django.shortcuts import render
from django.urls import resolve
from scripts import connect, microtik
from branches.models import Server, Branch, Reception, QA
from auth.about import *
# Create your views here.


def index(request):
    ip = None
    resolver_match = resolve(request.path_info)
    url_name = resolver_match.url_name  # Содержит имя URL-шаблона
    value = request.POST.get('input_mac')

    # # тут коннект к овпн
    if request.POST.get('button') == "ovpn":
        connect.connect(connect.ovpn[url_name])
        
    # тут получить айпи по маку у микрота
    if value:
        ip = microtik.get_ip(microtik.mcrtk[url_name], value)

    # В data только те записи которые соответствуют имени урла. фильтрация по полю branch
    try:
        branch_id = Branch.objects.get(name=url_name).id
        data = Server.objects.filter(branch=branch_id)
        r_data = Reception.objects.filter(branch=branch_id)

    except:
        data = None
        r_data = None

    contex = {'url_name': url_name, 'ip': ip, 'data': data, 'r_data': r_data}
    template_name = '.'.join((url_name, 'html')) # имена темплейтов соответствуют именам урлов
    return render(
        request,
        template_name,
        contex
    )

def qa(request):
    try:
        data = QA.objects.all()
    except:
        data = None
    contex = {'data': data}
    template_name = 'qa.html' # имена темплейтов соответствуют именам урлов
    return render(
        request,
        template_name,
        contex
    )


# def gagarina(request):
#     return render(request, 'gagarina.html', {'g_text': g_text, 'g': g})

