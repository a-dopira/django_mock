from django.shortcuts import render


def simple_view(request):
    context = {
        'title': 'Main page is here'
    }
    return render(request, 'notes/notes.html', context=context)
