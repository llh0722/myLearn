from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils.safestring import mark_safe
from untils import page

from myfirstapp import models
import json
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
        uid = request.POST.get('uid')
        # print(uid)
        cap = request.POST.get('cap')
        # print(cap)
        models.UserGroup.objects.filter(uid=uid).update(caption=cap)
        return redirect('/user_group')
    else:
        return redirect('/groupEdit')

# 删除用户组
def groupDel(request, nid):
    models.UserGroup.objects.filter(uid=nid).delete()
    return redirect('/user_group')

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

# 展示业务部门信息
def business_info(request):
    # 获取单表数据的三种方式
    # 对象
    bus_obj = models.Business.objects.all()
    # 字典
    bus_dic = models.Business.objects.all().values('bid', 'caption')
    # 元组
    bus_list = models.Business.objects.all().values_list('bid', 'caption')
    return render(request, 'business_info.html',
                  {"bus_obj": bus_obj,
                   "bus_dic": bus_dic,
                   "bus_list": bus_list
                   })

# 展示主机信息及添加新的记录
def host_info(request):
    if request.method == 'GET':
        # 对象
        host_obj = models.HOST.objects.filter(id__gt=0)
        # for row in host_obj:
        #     print(row.hostName, row.bid.caption)
        # 字典
        host_dic = models.HOST.objects.all().values('hostName', "bid__caption")
        # 元组
        host_list = models.HOST.objects.all().values_list('hostName', "bid__caption")
        business = models.Business.objects.all()
        return render(request, 'host_info.html',
                      {"host_obj": host_obj,
                       "host_dic": host_dic,
                       "host_list": host_list,
                       "business": business
                       })
    elif request.method == "POST":
        hostname = request.POST.get('hostName')
        ip = request.POST.get('ip')
        port = request.POST.get('port')
        bid_id = request.POST.get('bus_id')
        models.HOST.objects.create(
            hostName=hostname,
            ip=ip,
            port=port,
            bid_id=bid_id
        )
        return redirect('/host_info')
    else:
        return redirect('/host_info')

# ajax测试
def ajax_test(request):
    ret = {"status": True, "error_msg": None, "data": None}
    try:
        host = request.POST.get("hostname")
        ip = request.POST.get("ip")
        port = request.POST.get("port")
        bid = request.POST.get("bus_id")
        print(host, ip, port, bid)
        if host and len(host) > 5:
            models.HOST.objects.create(
                hostName=host,
                ip=ip,
                port=port,
                bid_id=bid
            )
        else:
            ret["status"] = False
            ret["error_msg"] = "太短了"
    except Exception as e:
        ret["status"] = False
        ret["error_msg"] = "请求错误"
    return HttpResponse(json.dumps(ret))

def app_host(request):
    if request.method == "GET":
        app_list = models.Application.objects.all()
        host_list = models.HOST.objects.all()
        return render(request, "app_host.html",
                      {"app_list": app_list,
                       "host_list": host_list
                       })
    elif request.method == "POST":
        a_name = request.POST.get("a_name")
        host_list = request.POST.getlist("host_list")
        print(a_name, host_list)
        app_obj = models.Application.objects.create(aname=a_name)
        app_obj.relation.add(*host_list)
        return redirect("/app_host")


def app_host_ajax(request):
    ret = {"status": True, "error_msg": None, "data": None}
    try:
        a_name = request.POST.get("a_name")
        host_list = request.POST.getlist("host_list")
        print(a_name, host_list, len(a_name))
        if a_name and len(a_name) > 2:
            app_obj = models.Application.objects.create(aname=a_name)
            app_obj.relation.add(*host_list)
        else:
            ret["status"] = False
            ret["error_msg"] = "太短了"
    except Exception as e:
        ret["status"] = False
        ret["error_msg"] = "请求错误"
    return HttpResponse(json.dumps(ret), content_type='application/json')

def app_del(request,nid):
    models.Application.objects.filter(id=nid).delete()
    return redirect("/app_host")


# 模板之继承
def tpl1(request):
    user_list = [1, 2, 3, 4]
    return render(request, "tpl1.html", {"user_list": user_list})

def tpl2(request):
    name = "DFJDGKDGjsdkfskd"
    return render(request, "tpl2.html", {"name": name})


List = []
for i in range(370):
    List.append(i)

def paging(request):
    # 获取当前页
    current_page = request.GET.get("page", 1)
    current_page = int(current_page)
    page_obj = page.Page(current_page, len(List))
    data = List[page_obj.start:page_obj.end]
    page_str = page_obj.page_str
    return render(request, "paging.html", {"data": data, "page_str": page_str})

















