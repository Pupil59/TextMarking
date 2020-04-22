from django.shortcuts import render


# Create your views here.
def showIndex(request):
    return render(request, template_name='textMark/index.html')


def showMain(request):
    return render(request, template_name='textMark/main.html')


def showGraph(request):
    return render(request, template_name='textMark/mgraph.html')


def showReg(request):
    return render(request, template_name='textMark/loginRegister.html')