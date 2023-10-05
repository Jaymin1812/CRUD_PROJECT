from django.shortcuts import render
from .forms import studentragistration 
from .models import User
# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm = studentragistration(request.POST)
        if fm.is_valid():
         
#  ==================================================================
# ------------------    -METHOD  NO:-1    ----------------------
#  ==================================================================

        #  fm.save()   ---------- AA Method thi pan Data ne Database(Admin) Joi shakay che 
        # ===============


#  ==================================================================
# ------------------    -METHOD  NO:-2    ----------------------
#  ===================================================================


#          nm=fm.cleaned_data['name']
#          em=fm.cleaned_data['email']
#          pw=fm.cleaned_data['password']
#          reg=User(name=nm, email=em ,password=pw)
#          reg.save()

# ===========================================================================================
#  --------------- AA Method thi pan Data ne Database(Admin) Joi shakay che -----------------
# ===========================================================================================

         nm=fm.cleaned_data['name']
         em=fm.cleaned_data['email']
         pw=fm.cleaned_data['password']
         reg=User(name=nm, email=em ,password=pw)
         reg.save()

#  ===========================================================================================================================================
#  fm = studentragistration()---------- AA Method thi Register/Login karelo data submit button per click karta CLEN thai jase ------------------    -METHOD    ----------------------
# =======================================================================================================================================
         fm = studentragistration()
# =========================================================================================================================================  

    else:
        fm = studentragistration()
    stud=User.objects.all()
    return render(request,'enroll/addendshow.html',{'form':fm , 'stu':stud})