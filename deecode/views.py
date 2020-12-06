from django.shortcuts import render
from . import code2
from . import decorder




def home(request):
    if request.method == 'POST':
        try:
            code_input = request.POST['codeinput']
            codeout = decorder.main_code(code_input)
            return render(request, 'home.html',{'codeoutput':codeout})
        except:
            text_input = request.POST['textinput']
            textout = code2.main_code(text_input)
            return render(request, 'home.html',{'textoutput':textout})
            
        print(code_input, text_input , 'Hello')
    else:
        return render(request, 'home.html') 

def about(request):
    return render(request, 'about.html')
