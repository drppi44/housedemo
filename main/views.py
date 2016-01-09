from annoying.decorators import render_to, ajax_request
from crispy_forms.utils import render_crispy_form
from django.template.loader import render_to_string
from main.filters import FlatFilter, HouseFilter
from main.forms import FlatForm, HouseForm
from django.core.context_processors import csrf
from main.models import Flat, House


@render_to('index.html')
def home(request):
    return {
        'form_house':  HouseForm(),
        'form_flat': FlatForm(),
        'flats': Flat.objects.all(),
        'houses': House.objects.all(),
        'filter': FlatFilter(request.GET, queryset=Flat.objects.all())
    }


@ajax_request
def flat_add(request):
    form = FlatForm(request.POST, request.FILES)
    ctx = {}
    ctx.update(csrf(request))
    form_html = render_crispy_form(form, context=ctx)
    if form.is_valid():
        form.save()
        return {'success': True, 'form_html': form_html}
    return {'success': False, 'form_html': form_html}


@ajax_request
def house_add(request):
    form = HouseForm(request.POST, request.FILES)
    ctx = {}
    ctx.update(csrf(request))
    form_html = render_crispy_form(form, context=ctx)
    if form.is_valid():
        form.save()
        return {'success': True, 'form_html': form_html}
    return {'success': False, 'form_html': form_html}


@ajax_request
def filter_flat(request):
    f = FlatFilter(request.POST, queryset=Flat.objects.all())
    h = HouseFilter(request.POST, queryset=House.objects.all())
    html_ = render_to_string('products.html', {'flats': f, 'houses': h})
    return {'html': html_}