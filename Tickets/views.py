from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.
import openpyxl
from .models import State,UserMaster,TaskMaster
from django.http import HttpResponse
from django.db import transaction
from .serializers import TaskMasterSerializer
from django.http import JsonResponse
import io
# @api_view(['POST'])
def parser(request):
    if request.method=="GET":
        file="C:\\Users\Maqsood\\Desktop\\Django_Todo\\Project_Minute\\states.xlsx"
        workbook = openpyxl.load_workbook(file)
        sheet = workbook.active
        for row in sheet.iter_rows(min_row=2,values_only=True):
            print(row)
            states,state_code=row
            d_state=State.objects.filter(state_name=states).first()
            if d_state:
                continue
            update=State(state_name=states,state_code=state_code)
            update.save()
        return HttpResponse("updated")
    # return 'Something wen wrong'
# parser('C:\\Users\\Maqsood\\Desktop\\Django_Todo\\Project_Minute\\Tickets\\states.xlsx')
# data = open("C:\\Users\Maqsood\\Desktop\\Django_Todo\\Project_Minute\\states.xlsx","r")
# parser("C:\\Users\Maqsood\\Desktop\\Django_Todo\\Project_Minute\\states.xlsx")

def userMasterView(request):
    if request.method=="GET":
        file="C:\\Users\Maqsood\\Desktop\\Django_Todo\\Project_Minute\\MOCK_DATA.xlsx"
        workbook = openpyxl.load_workbook(file)
        sheet = workbook.active
        a=0
        state = State.objects.all()
        state_length = len(state)
        for row in sheet.iter_rows(min_row=2,values_only=True):
            name,email,password,phone,city,gender,joining_date=row
            check=UserMaster.objects.filter(name=name,email=email,phone=phone,joining_date=joining_date)
            if check:
                continue
            print(state[0].id)
            data_updating=UserMaster(name=name,email=email,password=password,phone=phone,
            city=city, gender=gender, joining_date=joining_date, state=state[a])
            data_updating.save()
            a+=1
            if a==(state_length):
                a=0
            print(a)
        return HttpResponse("Done")
    
def UserMasterBulkDataView(request):
    if request.method =="GET":
        file="C:\\Users\Maqsood\\Desktop\\Django_Todo\\Project_Minute\\MOCK_DATA2.xlsx"
        workbook = openpyxl.load_workbook(file)
        sheet = workbook.active
        a=0
        state = State.objects.all()
        state_length = len(state)
        user_data=[]
        for row in sheet.iter_rows(min_row=2,values_only=True):
            name,email,password,phone,city,gender,joining_date=row
            check=UserMaster.objects.filter(name=name,email=email,phone=phone,joining_date=joining_date)
            if check:
                continue
            data_updating=UserMaster(name=name,email=email,password=password,phone=phone,
            city=city, gender=gender, joining_date=joining_date, state=state[a])
            user_data += [data_updating]
            a+=1
            if a==(state_length):
                a=0
        with transaction.atomic():
            UserMaster.objects.bulk_create(user_data)
        return HttpResponse("Done")


def task(request):
    if request.method=="POST":
        task_id=request.POST.get('taskid')
        title=request.POST.get('title')
        description=request.POST.get('description')
        assign_date=request.POST.get('assign_date')
        state=request.POST.get('state')
        assign_to=request.POST.get('assign_to')

        check_assign_to=UserMaster.objects.filter(id=assign_to)
        check_state=State.objects.filter(state_name=state)
        print(check_assign_to)
        print(check_state)
        if check_assign_to and check_state:
            data=TaskMaster(task_id=task_id,title=title,
                            description=description,assign_date=assign_date,
                            state=check_state[0],user_id=check_assign_to[0])
            data.save()
        else:
            return HttpResponse("Something went wrong")

    return render(request,"index.html")

def ManipulateTasks(request,id=None):
    if request.method == "GET":
        tasks = TaskMaster.objects.all().order_by('id')
        serializer = TaskMasterSerializer(tasks, many=True)
        serialized_data = serializer.data
        
    return render(request, 'ViewAssignedTask.html', {'data': serialized_data})

    # if request.method == "DELETE":
       
# Add this view to your views.py
from django.shortcuts import get_object_or_404, redirect

def DeleteTask(request, id):
    task = get_object_or_404(TaskMaster, id=id)
    task.delete()
    return redirect('view-tasks')


def update(request,id):
    
    task = get_object_or_404(TaskMaster,id=id)
    if request.method=="POST":
        print(task.assign_date)
        if id:
            task_id=request.POST.get('taskid')
            title=request.POST.get('title')
            description = request.POST.get('description')
            assign_date = request.POST.get('assign_date')
            if assign_date:
                task.assign_date=assign_date
            task.task_id=task_id
            task.title=title
            task.description=description
            

            task.save()
            return redirect('view-tasks')
    return render(request, 'update.html', {'task': task})


