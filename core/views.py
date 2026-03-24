from django.shortcuts import render


def home_view(request):
    """
    BizBozor bosh sahifasi.
    Hozircha oddiy home.html render qilamiz.
    """
    return render(request, 'home.html')