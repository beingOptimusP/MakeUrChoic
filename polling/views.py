from django.shortcuts import render,HttpResponse,redirect
from .models import CreatPoll,OpenPoll
from .forms import PollForm
from django.core.mail import send_mail as sm

# Create your views here.
def index(request):
    return render(request,'index.html')

def create(request):
    if request.method == 'POST':
        select=request.POST['polltype']

        title=request.POST['Title']
        o1=request.POST['o1']
        o2=request.POST['o2']
        o3=request.POST['o3']
        o4=request.POST['o4']

        create=CreatPoll(Title=title,o1=o1,o2=o2,o3=o3,o4=o4)
        create.save()
            
        

        return redirect('Tpolls')
    else:
        form = PollForm()
        

    form=PollForm()
    context={
        'form':form
    }
    return render(request,'createpoll.html',context)


def Tpolls(request):
    objects=CreatPoll.objects.all()
    # objects_Open=OpenPoll.objects.all()
    context={
        'poll':objects
    }
    return render(request,'Tpolls.html',context)

def CreatePoll(request,poll_id):
    if request.method == 'POST':

        poll=CreatPoll.objects.get(pk=poll_id)
        on1=int(request.POST['on1'])
        on2=int(request.POST['on2'])
        on3=int(request.POST['on3'])
        on4=int(request.POST['on4'])

        if on1==1:
            poll.one_1+=1
        if on2==1:
            poll.two_1+=1
        if on3==1:
            poll.three_1+=1
        if on4==1:
            poll.four_1+=1


        poll.on1+=int(request.POST['on1'])
        poll.on2+=int(request.POST['on2'])
        poll.on3+=int(request.POST['on3'])
        poll.on4+=int(request.POST['on4'])
        poll.save()
    
        return redirect('Tpolls')
    poll=CreatPoll.objects.get(pk=poll_id)
    context={
        'poll':poll
    }
    return render(request,'poll.html',context)


def pollResult(request,poll_id):
    poll=CreatPoll.objects.get(pk=poll_id)
    
    arr=[poll.on1,poll.on2,poll.on3,poll.on4]

    Ar=[poll.one_1,poll.two_1,poll.three_1,poll.four_1]

    a=[poll.o1,poll.o2,poll.o3,poll.o4]
    
    x=arr.index(min(arr))

    win=a[x]

    for i in arr:
        if arr[x]==i:
            if Ar[x]>Ar[arr.index(i)]:
                win=a[x]
            else:
                win=a[arr.index(i)]

        context={
        'poll':poll,
        'win':win 
    }


    return render(request,'pollresult.html',context)

def Teams(request):
    return render(request,'team.html')


def OpenPoll(request,poll_id):
    # if request.method == 'POST':

    #     poll=OpenPoll.objects.get(pk=poll_id)
    #     on1=int(request.POST['on1'])
    #     on2=int(request.POST['on2'])
    #     on3=int(request.POST['on3'])
    #     on4=int(request.POST['on4'])


    #     poll.on1+=int(request.POST['on1'])
    #     poll.on2+=int(request.POST['on2'])
    #     poll.on3+=int(request.POST['on3'])
    #     poll.on4+=int(request.POST['on4'])
    #     poll.save()
    
    #     return redirect('Tpolls')
    # poll=CreatPoll.objects.get(pk=poll_id)
    # context={
    #     'poll':poll
    # }
    return render(request,'openpoll.html',context)
    

