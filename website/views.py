from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'website/LandingPage.html')

def WPET(request):
    return render(request, 'website/projectinfo.html')

def QandA(request):
    return render(request, 'website/QandA.html')

def teaminfo(request):
    return render(request, 'website/teaminfo.html')

def milestone(request):
    return render(request, 'website/milestone.html')
