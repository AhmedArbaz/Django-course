
#ya same main url.py say copy ki hay aur yaha lay hain ya sub url file hay jis ko main url file may dalna hota hay jo kay ham nay 1st day diragram may dakha tha kay urls.py jo hay vo urls.py ko hi refer kr rahi thi ya hay vo case kay main urls.py apps ki urls.py ko refer karti hay

from django.urls import path
from . import views
urlpatterns = [
    #same name dain gay jo views may diay thay like ,home Or HOME asay  
    
    #url define ho gaya kasay 
    #localhost:8000/firstApp  -> ya ham nay kia hay main url file firstapp day rahi hay rout may yaha ham nay kuch nahi dia ager hamin firstApp/order chiay to yaha order/ day do kuch asay 
    
    # path('order/', views.all_chai,name='order'),
    
    
    path('', views.all_chai,name='all_chai'), #ya ham nay home route define kar dia ya only name dia hay
    
]
