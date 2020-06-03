from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from myfirstapp import models
# Create your views here.

def login(request):
    # error_msg = ''
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        obj = models.UserInfo.objects.filter(username=user, password=pwd).first()
        if obj:
            return redirect('index.html')
        else:
            error_msg = '用户名或密码错误'
            return render(request, 'login.html', {'error_msg': error_msg})
    else:
        return redirect('index.html')

def user_info(request):
    if request.method == 'GET':
        user_list = models.UserInfo.objects.all()
        group_list = models.UserGroup.objects.all()
        return render(request, 'user_info.html',
                      {"user_list": user_list},
                      {"group_list": group_list}
                      )
    elif request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        email = request.POST.get('email')
        models.UserInfo.objects.create(
            username=user,
            password=pwd,
            email=email
        )
        return redirect('/user_info')
    else:
        return redirect('/user_info')

def user_group(request):
    pass

'''
user_dict = {
    '1': {'name': 'alex', 'email': 'alex@163.com'},
    '2': {'name': 'mary', 'email': 'mary@163.com'},
    '3': {'name': 'lily', 'email': 'lily@163.com'},
}
'''

def index(request):
    return render(request, 'index.html')

def detail(request,nid):
    obj = models.UserInfo.objects.filter(id=nid).first()
    return render(request, 'detail.html', {'obj': obj})
    '''
        nid = request.GET.get('nid')
        return HttpResponse(nid)
        detail_info = user_dict[nid]
        return render(request, 'detail.html', {'detail_info': detail_info})
        '''

def userDel(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user_info')

def userEdit(request, nid):
    if request.method == 'GET':
        obj = models.UserInfo.objects.filter(id=nid).first()
        return render(request, 'userEdit.html', {"obj": obj})
    elif request.method == 'POST':
        nid = request.POST.get('id')
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        models.UserInfo.objects.filter(id=nid).update(
            username=user, password=pwd
        )
        return redirect('/user_info')


def orm(request):
    # 创建方法一
    # models.UserInfo.objects.create(username='alex', password=123)

    # 创建方法二
    '''
    dict = {'username': 'mary', 'password': '456'}
    models.UserInfo.objects.create(**dict)
    '''
    # 创建方法三
    '''
    obj = models.UserInfo(username='lily', password=789)
    obj.save()
    '''

    # 查询
    # result = models.UserInfo.objects.all()   # 查找所有  queryset类型
    # result = models.UserInfo.objects.filter(username='alex')  # 条件查询
    # for row in result:
    #     print(row.id, row.username, row.password)
    # print(result)

    # 删除
    # models.UserInfo.objects.filter(username='lily').delete()

    # 更新
    # models.UserInfo.objects.filter(username='alex').update(password=666)

    # 一对多
    '''
    models.UserInfo.objects.create(
        username='alex',
        password='123',
        email='123@163.com',
        user_type_id=1,
        user_group_id=1,
    )
    '''
    # 修改
    models.UserInfo.objects.filter(id=2).update(
        username='mary',
        password='456',
        email='456@163.com',
        user_type_id=2,
    )

    return HttpResponse('orm')


