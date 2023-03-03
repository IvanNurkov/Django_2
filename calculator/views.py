from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def omlet(request):
    serving = int(request.GET.get('serving', 1))
    context = {
        'recipe': {
        }
    }
    for key, val in DATA.items():
        if key == 'omlet':
            context['recipe'] = val
            for k, v in val.items():
                v_1 =  v * serving
                context['recipe'][k] = v_1
    return render(request, 'calculator/index.html', context)

def pasta(request):
    serving = int(request.GET.get('serving', 1))
    context = {
        'recipe': {
        }
    }
    for key, val in DATA.items():
        if key == 'pasta':
            context['recipe'] = val
            for k, v in val.items():
                v_1 =  v * serving
                context['recipe'][k] = v_1
    return render(request, 'calculator/index.html', context)


def buter(request):
    serving = int(request.GET.get('serving', 1))
    context = {
        'recipe': {
        }
    }
    for key, val in DATA.items():
        if key == 'buter':
            context['recipe'] = val
            for k, v in val.items():
                v_1 = v * serving
                context['recipe'][k] = v_1
        return render(request, 'calculator/index.html', context)
    return render(request, 'calculator/index.html', context)

