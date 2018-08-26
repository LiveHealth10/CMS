from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import StudentIdForm
from django.template import loader



def check(request):
    try:

        if request.session['auth']=='Parent':
            if request.method=='POST':
                form=StudentIdForm(request.POST)
                if form.is_valid:
                    id=request.POST.get('id')
                    request.session['stuid']=id
                    return HttpResponseRedirect('/home/student/')
                
            else:
                form=StudentIdForm()
            
            return render(request,'parent.html',{'form':form})
        else:
            request.session.flush()
            return HttpResponseRedirect('/home/')
    except KeyError:
        request.session.flush()
        return HttpResponseRedirect('/home/')
