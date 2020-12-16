from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from user.models import sensor_table,User
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt, csrf_protect
# from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.api.serializers import userSerializers,sensorSerializer



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = userSerializers
    #permission_classes = [permissions.IsAuthenticated]


class SensorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = sensor_table.objects.all()
    serializer_class = sensorSerializer
 #   permission_classes = [permissions.IsAuthenticated]

#class sensorList(APIView):

def get(request):
    sensorlist=sensor_table.objects.all()
    print(sensorlist)
        # serializer = sensorSerializer(sensorlist,many=True)
        # return response(serializer.data)


##################################################################
####################index#######################################
def login(request):
    return render(request, 'user/main.html')

########################################################################
########### register here #####################################
@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            #########################mail####################################
            htmly = get_template('user/Email.html')
            d = { 'username': username }
            subject, from_email, to = 'hello', 'from@example.com', 'to@emaple.com'
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            try:
                msg.send()
            except:
                print("error in sending mail")
            ##################################################################
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form,'title':'reqister here'})

###################################################################################
################login forms###################################################

def Login(request):
    if request.method == 'POST':

        #AuthenticationForm_can_also_be_used__

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request,user)
            messages.success(request, f' welcome {username} !!')
            return redirect('index')
        else:
            messages.info(request, 'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/main.html', {'form':form,'title':'log in'})


def index(request):
    return render(request,'user/main.html')
#
# def data(request):
#     result=SensorData.objects.all()
#     return render(request,"user/Testing.html",{'SensorData':result})