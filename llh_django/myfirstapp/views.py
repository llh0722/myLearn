from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from myfirstapp import models
# Create your views here.
# 登录
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

'''
用户
'''
# 用户列表展示及添加用户
def user_info(request):
    if request.method == 'GET':
        user_list = models.UserInfo.objects.all()
        group_list = models.UserGroup.objects.all()
        return render(request, 'user_info.html', {"user_list": user_list, "group_list": group_list})
    elif request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        email = request.POST.get('email')
        nid = request.POST.get('group_id')
        models.UserInfo.objects.create(
            username=user,
            password=pwd,
            email=email,
            user_group_id=nid,
        )
        return redirect('/user_info')
    else:
        return redirect('/user_info')

'''
user_dict = {
    '1': {'name': 'alex', 'email': 'alex@163.com'},
    '2': {'name': 'mary', 'email': 'mary@163.com'},
    '3': {'name': 'lily', 'email': 'lily@163.com'},
}
'''

# 用户管理系统首页
def index(request):
    return render(request, 'index.html')

# 用户详细信息
def detail(request,nid):
    obj = models.UserInfo.objects.filter(id=nid).first()
    return render(request, 'detail.html', {'obj': obj})
    '''
        nid = request.GET.get('nid')
        return HttpResponse(nid)
        detail_info = user_dict[nid]
        return render(request, 'detail.html', {'detail_info': detail_info})
        '''

# 用户删除
def userDel(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user_info')

# 用户编辑
def userEdit(request, nid):
    if request.method == 'GET':
        obj_user = models.UserInfo.objects.filter(id=nid).first()
        obj_group = models.UserGroup.objects.filter(uid=obj_user.user_group_id).first()
        group_list = models.UserGroup.objects.all()
        return render(request, 'userEdit.html',
                      {"obj_user": obj_user,
                       "obj_group": obj_group,
                       "group_list": group_list
                       })
    elif request.method == 'POST':
        nid = request.POST.get('id')
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        email = request.POST.get('email')
        uid = request.POST.get('group_id')
        # print(uid)
        models.UserInfo.objects.filter(id=nid).update(
            username=user,
            password=pwd,
            email=email,
            user_group_id=uid
        )
        return redirect('/user_info')
    else:
        return redirect('/userEdit')

'''
用户组
'''
# 用户组列表展示及添加用户组
def user_group(request):
    if request.method == 'GET':
        group_list = models.UserGroup.objects.all()
        return render(request, 'user_group.html', {"group_list": group_list})
    elif request.method == 'POST':
        cap = request.POST.get('caption')
        models.UserGroup.objects.create(caption=cap,)
        return redirect('/user_group')
    else:
        return redirect('/user_group')

# 编辑用户组
def groupEdit(request, nid):
    if request.method == 'GET':
        obj_group = models.UserGroup.objects.filter(uid=nid).first()
        return render(request, 'groupEdit.html', {"obj_group": obj_group})
    elif request.method == 'POST':
        nid = request.POST.get('id')
        # print(uid)
        cap = request.POST.get('caption')
        models.UserGroup.objects.filter(id=nid).update(caption=cap)
        return redirect('/user_group')
    else:
        return redirect('/groupEdit')

# 删除用户组



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

