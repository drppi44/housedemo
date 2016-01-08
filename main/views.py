from annoying.decorators import render_to, ajax_request
from crispy_forms.utils import render_crispy_form
from main.forms import FlatForm, HouseForm
from django.core.context_processors import csrf


@render_to('index.html')
def home(request):
    return {'form_house':  HouseForm(), 'form_flat': FlatForm()}


@render_to('flat.html')
def flat(request):
    form = FlatForm()
    return {'form': form}


@ajax_request
def flat_add(request):
    form = FlatForm(request.POST or None)
    if form.is_valid():
        form.save()
        return {'success': True}

    ctx = {}
    ctx.update(csrf(request))
    form_html = render_crispy_form(form, context=ctx)
    return {'success': False, 'form_html': form_html}


@ajax_request
def house_add(request):
    form = HouseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return {'success': True}

    ctx = {}
    ctx.update(csrf(request))
    form_html = render_crispy_form(form, context=ctx)
    return {'success': False, 'form_html': form_html}
