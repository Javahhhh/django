from app01.models import Upcontent
from app01 import models
from app01.models import Department, UserInfo
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from .models import Upcontent

# Create your views here.
def index(request):
    return HttpResponse('玩儿')


def user_list(request):
    return render(request, 'user_list.html')


def login(request):
    if request == "GET":
        return render(request, 'login.html')

        # print(request.POST)
    username = request.POST.get("user")
    password = request.POST.get("pwd")

    if username == 'root' and password == '123':
        # return HttpResponse("登录成功")
        return redirect("https://www.bilibili.com/")

    #  return HttpResponse("登录失败")
    return render(request, 'login.html', {"用户名或密码错误"})


def orm(request):
    # Department.objects.create(title="超人部")
    # Department.objects.create(title="超人2部")
    # Department.objects.create(title="超人6部")
    # UserInfo.objects.create(name='迪迦',age='05')
    # UserInfo.objects.create(name='迪迦奥特曼',age='6')
    # UserInfo.objects.all().delete()

    # 3.获取数据
    # data_list = UserInfo.objects.all()
    # for obj in data_list:
    #     print(obj.id,obj.name,obj.password,obj.age)
    # data_list=UserInfo.object.filter(id=1)
    # print(data_list)
    # 3.1 获取第一条数据
    # row_obj=UserInfo.objects.filter(id=1).first()
    # print()

    # 4更新数据
    # UserInfo.objects.filter(id=2).update(age=6)
    Upcontent.objects.create
    return HttpResponse("SUCCESS")


# 重要例子


def info_list(request):
    # 获取所有用户信息
    data_list = UserInfo.objects.all()
    # print(data_list)

    return render(request, "info_list.html", {"data_list": data_list})


def info_add(request):
    if request.method == "GET":
        return render(request, 'info_add.html')

    # 获取用户提交的数据
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")

    # 添加到数据库
    UserInfo.objects.create(name=user, password=pwd, age=age)

#    return redirect("http://127.0.0.1:8000/info/list/")
    return redirect("/info/list/")


def info_delete(request):
    nid = request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()
    # return HttpResponse("删除成功")
    return redirect("/info/list/")


def sign_in(request):
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")

    UserInfo.objects.create(name=user, password=pwd)
    return redirect("")


def home(request):
    contents = Upcontent.objects.order_by('id')
   
    return render(request, 'home.html',{'contents':contents} )

def sign_in(request):

        return render(request, 'sign_in.html')


# def publish_content(request):
#     if request.method == 'GET':
#         return render(request,'publish_content.html')
#     title = request.POST.get('title')
#     text = request.POST.get('content')
#     Upcontent.objects.create(title=title, text=text)
#     return render(request, 'home.html')

    # if request.method == 'POST':
    #     form = PublishContentForm(request.POST)
    #     if form.is_valid():
    #         # 提取标题和内容
    #         title = form.cleaned_data['title']
    #         text = form.cleaned_data['text']
            
    #         # 将数据保存到 Upcontent 模型中
    #         Upcontent.objects.create(title=title, text=text)
            
    #         # 重定向到主页
    #         return redirect('/home/')
    # else:
    #     # 渲染发布内容的表单
    #     form = PublishContentForm()

    # # 渲染模板
    # return render(request, '/home', {'form': form})
def publish_content(request): 
   
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        action = request.POST.get('action')
        Upcontent.objects.create(title=title, text=text)
        return redirect('/home')
        
    return render(request, 'publish_content.html')
   
   
def administrator(request):
    return render(request,'administrator.html')       



def receive_content(request, content_id):
    text_data = Upcontent.objects.get(id=content_id)
    return render(request, 'receive_content.html', {'text_data': text_data})

def article_detail(request,id):
    
    
    article=Upcontent.objects.get(id=id)
    context={'article':article}
    return render(request,'article_detail.html',context)

# def create_article(request):
#     if request.method == "POST":
#         # 获取表单数据
#         title = request.POST.get("title")
#         content = request.POST.get("content")
#         # 创建新的文章
#         article = Article(title=title, content=content)
#         article.save()
#         # 跳转到新发布的文章详细信息页面
#         return redirect("mysite:article_detail", article.id)
#     return render(request, "create.html")

# def mysite(request):
#     contents = Upcontent.objects.order_by('id')    
#     return render(request, 'mysite.html',{'contents': contents} )
    