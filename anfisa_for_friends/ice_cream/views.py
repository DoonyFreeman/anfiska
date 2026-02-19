from django.shortcuts import render, get_object_or_404, Http404

from .models import IceCream


# fallback dataset used only when the database is empty
_default_catalog = [
    {
        'id': 0,
        'title': 'Классический пломбир',
        'description': 'Настоящее мороженое, для истинных ценителей вкуса. '
                       'Если на столе появляется пломбир — это не надолго.',
        'price': '100.00',
        'is_available': True,
    },
    {
        'id': 1,
        'title': 'Мороженое с кузнечиками',
        'description': 'В колумбийском стиле: мороженое '
                       'с добавлением настоящих карамелизованных кузнечиков.',
        'price': '150.00',
        'is_available': True,
    },
    {
        'id': 2,
        'title': 'Мороженое со вкусом сыра чеддер',
        'description': 'Вкус настоящего сыра в вафельном стаканчике.',
        'price': '120.00',
        'is_available': False,
    },
]


def ice_cream_detail(request, pk):
    template = 'ice_cream/detail.html'
    try:
        ice_cream = IceCream.objects.get(pk=pk)
    except IceCream.DoesNotExist:
        # if no database object, see if fallback entry exists
        ice_cream = next((item for item in _default_catalog if item['id'] == pk), None)
        if ice_cream is None:
            raise Http404("IceCream not found")
    context = {'ice_cream': ice_cream}
    return render(request, template, context)


def ice_cream_list(request):
    template = 'ice_cream/list.html'
    qs = IceCream.objects.filter(is_available=True)
    if not qs.exists():
        # database empty – show fallback examples and a notice in template
        context = {'ice_cream_list': _default_catalog, 'fallback': True}
    else:
        context = {'ice_cream_list': qs}
    return render(request, template, context)
