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


def showUserInfo(request):
    return render(request, template_name='textMark/user-info.html')


def showMsgList(request):
    return render(request, template_name='textMark/msglist.html')


def showMsgList(request):
    return render(request, template_name='textMark/msglist.html')


def showInvite(request):
    return render(request, template_name='textMark/invite.html')

def showExport(requst):
    return render(request, template_name='textMark/export.html')
