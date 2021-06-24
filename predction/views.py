from django.shortcuts import render

import numpy as np
from tensorflow.keras.models import load_model


# Create your views here.

def Index(request):

    return render(request,'index.html')




def Result(request):
    model_file = 'housingprice.h5'
    model = load_model(model_file)
    # print(request.GET.get('area'))
    if request.method=='POST':
        list=[]
        list.append(int(request.POST.get('byear')))
        list.append(int(request.POST.get('flor')))
        list.append(int(request.POST.get('area')))
        list.append(int(request.POST.get('fbath')))
        list.append(int(request.POST.get('hbath')))
        list.append(int(request.POST.get('bedroom')))
        list.append(int(request.POST.get('troom')))
        list.append(int(request.POST.get('syear')))
        my_list=np.array(list)
        my_list=my_list.reshape(1,8)
        results=model.predict(my_list,batch_size=1)
        return render(request,'result.html',context={'ans':results})
