from django.shortcuts import render


def home(request):
    """Контроллер для отображения домашней страницы"""

    return render(request, 'home.html')


def contact(request):
    """Контроллер для отображения страницы контактов"""

    return render(request, 'contacts.html')
