from django.shortcuts import render

# Create your views here.

# the first way
# def home(request):

#     if request.method == 'POST':
#         h = request.POST.get('height')
#         w = request.POST.get('weight')
#         h = int(h)
#         w = int(w)
#         print(h, w)

#         bmi = round(w/(h/100)**2, 2)
#         return render(request, 'app_bmi/home.html', {'yourbmi': bmi})
    
#     return render(request, 'app_bmi/home.html')

# the second way : Ajax API POST
def home(request):
    return render(request, 'app_bmi/home.html')
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def api_get_bmi(request):
    try:
        height = int(request.POST.get('height'))
        weight = int(request.POST.get('weight'))
        result = round( weight / pow(height / 100, 2),  2)
        print(height, weight)
        response = {"yourbmi" : result}
        return JsonResponse(response)
    except:
        print("Not an legal ajax call")
        return JsonResponse({"yourbmi" : 'error'})


# # the third way : Ajax API GET
# def home(request):
#     return render(request, 'app_bmi/home.html')
# from django.http import JsonResponse
# def api_get_bmi(request):
#     try:
#         height = int(request.GET.get('height'))
#         weight = int(request.GET.get('weight'))
#         result = round( weight / pow(height / 100, 2),  2)
#         print(height, weight)
#         response = {"yourbmi" : result}
#         return JsonResponse(response)
#     except:
#         print("Not an legal ajax call")
#         return JsonResponse({"yourbmi" : 'error'})