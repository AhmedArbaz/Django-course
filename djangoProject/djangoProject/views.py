from django.http import HttpResponse
# ab ham req,res lay sakty hain jasay js may laty thay vasay yaha nahi hota hay 
from django.shortcuts import render
# ab hamin template banai hay aus ko render kay liya ais ko import kia 

def home(request):
    # return HttpResponse("Hello, world. You're at the home page.") 
    #phaya ya ata tha home route pay ab ham file/template ko render kara rahy hain 
    
    return render(request, 'website/index.html')#ham nay template may website folder bana dia ais may index.html dali to ab ais ko render kay liya ya to templates/website likh day to bhi kam ho jay ga ya views.py  may website/index.html dalin to bhi ho jay ga



def about(request):
    return HttpResponse("Hello, world. You're at the about page.")


def contact(request):
    return HttpResponse("Hello, world. You're at the contact page.")

# bas ya kam hota hay views.py may ab urls.py may jao