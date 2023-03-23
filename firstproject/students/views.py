from django.shortcuts import render,redirect

# Create your views here.
from students.models import student

def listone(request): 
    try: 
        unit = student.objects.get(stuName="111") #讀取一筆資料
    except:
        errormessage = " (讀取錯誤!)"
    return render(request, "listone.html", locals())

def listall(request):  
    allStudents = student.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
    return render(request, "listall.html", locals())

def post(request):  
    if request.method=="POST":
        mess="姓名:"+request.POST["stuName"]+"、學號:"+request.POST["stuID"]+"、性別:"+request.POST["stuSex"]+"、生日:"+request.POST["stuBirth"]+"、電子郵件:"+request.POST["stuEmail"]+"、手機號碼:"+request.POST["stuPhone"]+"、地址:"+request.POST["stuAddress"]
    else:
        mess="表單尚未送出!"
    return render(request,"addstudent.html",locals())

def post1(request):
    if request.method == "POST":      #如果是以POST方式才處理
        stuName = request.POST['stuName'] #取得表單輸入資料
        stuID = request.POST['stuID']
        stuSex =  request.POST['stuSex']
        stuBirth =  request.POST['stuBirth']
        stuEmail = request.POST['stuEmail']
        stuPhone =  request.POST['stuPhone']
        stuAddress =  request.POST['stuAddress']
        #新增一筆記錄
        unit = student.objects.create(stuName=stuName, stuID=stuID, stuSex=stuSex, stuBirth=stuBirth, stuEmail=stuEmail, stuPhone=stuPhone, stuAddress=stuAddress) 
        unit.save()  #寫入資料庫
        return redirect('/post1')  
    else:
        mess = '請輸入資料(資料不作驗證)'
    return render(request, "addstudent1.html", locals())
