from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render

from .models import Reporter
# Create your views here.


# def index(request):
#     latest_reporter_list = Reporter.objects.order_by('-id')[:5]
#     output = ', '.join([r.first_name for r in latest_reporter_list])
#     return HttpResponse(output)

##################
# For template
def index(request):
    latest_reporter_list = Reporter.objects.order_by('-id')[:5]
    # template = loader.get_template('emp_details/index.html')
    context = {
        'latest_reporter_list': latest_reporter_list,
    }
    # return HttpResponse(template.render(context, request))
    # for Render
    return render(request, 'emp_details/index.html', context)


def detail(request, reporter_id):
    try:
        reporter = Reporter.objects.get(pk=reporter_id)
    except Reporter.DoesNotExist:
        raise Http404("Reporter does not exist.")
    return render(request, 'emp_details/detail.html', {'reporter': reporter})