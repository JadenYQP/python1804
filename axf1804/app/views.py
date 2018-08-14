import hashlib
import uuid

from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.

# 这是主页
from django.urls import reverse

from app.models import HomeWheel, HomeNav, HomeMustbuy, HomeShop, HomeMainshow, marketFoodtypes, marketGoods, UserModel, \
    CartModel, orderModel, orderGoodsModel


def home(request):
    #获得轮播图数据
    wheels=HomeWheel.objects.all()
    #顶部nav导航数据
    navs=HomeNav.objects.all()
    # 必买产品数据
    mustbuys=HomeMustbuy.objects.all()
    #购物类型
    shops=HomeShop.objects.all()
    #将数据拆分
    shop1 = shops[0:1]
    shop2 = shops[1:3]
    shop3 = shops[3:7]
    shop4 = shops[7:]
    #产品shou展示
    mainShows=HomeMainshow.objects.all()
    data={
        "title":'主页',
        "wheels":wheels,
        "navs": navs,
        "mustbuys":mustbuys,
        "shop1": shop1,
        "shop2": shop2,
        "shop3": shop3,
        "shop4": shop4,
        "mainShows": mainShows
    }
    return render(request,'home/home.html',context=data)

##########################################33
# 超市
def market(request):

    return redirect(reverse("axf:marketWP",args=('104749','0','1')))

def market_with_param(request,typeid,childcid,sortType):
    #商品类型数据
    foodtypes = marketFoodtypes.objects.all()
    #商品所有数据
    # goods = marketGoods.objects.all()

    #根据商品类型来查询
    # goods=marketGoods.objects.filter(categoryid=typeid)

    #找到 childtypenames并拆分出来
    foodType=marketFoodtypes.objects.filter(typeid=typeid).first()

    childtypes=foodType.childtypenames.split('#')

    allchildType=[]

    for childtype in childtypes:

        type=childtype.split(":")    #  ["全部分类","0"]
        allchildType.append(type)

    if childcid == "0":
        # 根据商品类型来查询 0的时候代表所有商品
        goods=marketGoods.objects.filter(categoryid=typeid)
    else:
        goods = marketGoods.objects.filter(categoryid=typeid).filter(childcid=childcid)

    # 综合排序
    if sortType=='1':
        pass                    # 综合排序
    elif sortType == '2':
        goods = goods.order_by('productnum')                  # 排序销量
    elif sortType == '3':
        goods = goods.order_by('price')                        # 价格最低
    elif sortType == '4':
        goods = goods.order_by('-price')                       # 价格最高
    else:
        pass



    data = {
        "title": '超市',
        "foodtypes": foodtypes,
        "goods": goods,
        "typeid": typeid,
        "allchildType":allchildType
    }
    return render(request, 'market/market.html', context=data)

##############################################333
# 购物车
def cart(request):

    #判断用户是否存在,找到session的user_id
    user_id = request.session.get('user_id')
    # print(user_id)
    #没有first(),找到的是一类
    res=UserModel.objects.filter(pk=user_id)
    if not res.exists():    #不存在,返回登录页
        return  redirect(reverse("axf:logoUser"))
    user=res.first()


    #根据用户查询购物车
    carts=CartModel.objects.filter(c_user=user)
    is_allselect=True
    #只要有一个没选中,就置为False
    for cart in carts:
        # cart=CartModel()
        if cart.c_isselect==False:
            is_allselect = False
            break

    data = {
        "title": '购物车',
        "carts": carts,
        "is_allselect":is_allselect,

    }
    return render(request,'cart/cart.html',context=data)

##########################################
# 我的
def mine(request):
    # print(111111111111111)
    # 根据session获取user_id
    user_id=request.session.get('user_id')
    # print(user_id)
    # print(22222222222222222)
    #判断如果没有获取到,跳转到注册页面

    #根据user_id获取到对应的user
    res=UserModel.objects.filter(pk=user_id)
    user = None
    is_login = False
    imPath='#'
    #判断
    if res.exists():
        # print(33333333333333333333333333)
        # user=UserModel()
        user=res.first()
        is_login=True
        # user = UserModel()
        imPath="/static/media/" + user.icons.url
        # print(imPath)

    data = {
        "title": '我的',
        "user": user,
        "imPath": imPath,
        "is_login": is_login,
    }
    return render(request,'mine/mine.html',context=data)

# 注册请求
def register(request):
    method=request.method
    if method == "GET":  #注册请求页面
        return render(request, 'user/user_register.html')
    elif method == "POST": #执行注册
        #获取到上传的数据
        username=request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        icons = request.FILES["icons"]

        # print(username)
        # print(password)
        # print(email)
        # print(icons)

        #创建一个数据库对象,将获取到的数据存入数据库中
        userModel=UserModel()
        userModel.username=username
        userModel.password=createPwd(password)  #注意:密码进行再加密处理后存入数据库
        userModel.email=email
        userModel.icons=icons
        userModel.save()

        #设置session,存储userid
        request.session['user_id']=userModel.id

        return redirect(reverse('axf:mine'))


#密码处理
#对密码在进行加密处理
def createPwd(password):
    mysha512 = hashlib.sha512()
    mysha512.update(password.encode("utf-8"))
    return  mysha512.hexdigest()

#退出的函数
def logout(request):
    #清除session
    request.session.flush()
    return redirect(reverse("axf:mine"))


#验证用户名是否存在
def checkUser(request):
    #请求得到输入框中的用户名数据
    username=request.GET.get("username")
    #在数据库中筛选,根据框中的用户名数据筛选出,给一个结果,判断结果是否存在
    res=UserModel.objects.filter(username=username)
    data={}
    if res.exists():
        data["status"]="user is exist"
        data["msg"]="用户名已经存在,请重新设置"
        data["code"]="901"
    else:       #不存在
        data["status"] = "ok"
        data["msg"] = "用户名可用"
        data["code"] = "200"

    return JsonResponse(data)

#处理登录页面
def logoUser(request):
    #获得method进行判别
    method=request.method
    if method == "GET":  #请求登录页面
        return render(request, 'user/user_login.html')
    elif method == "POST":  #POST请求,获得输入框中的密码,用户名
        username = request.POST.get("username")
        # print(username)
        password = request.POST.get("password")
        # print(password)
        #验证账号和密码是否匹配,匹配后,跳转到我的页面,并且有登录的用户信息
        res=UserModel.objects.filter(username=username)
        #判断user是否存在
        if res.exists():
            # print(1111111111111111)
            user=res.first()
            # print(user)
            #判断密码
            # user=UserModel()
            # print(user.password)
            # print(createPwd(password))
            if user.password == createPwd(password):    #注意数据库的密码是两次加密后的存储值,比较时,
                # print(2222222222)
                #设置一个session,与view我的,进行匹配,跳转后头像,用户名变更
                request.session["user_id"]=user.id
                #重定向到mine页面
                return redirect(reverse("axf:mine"))    #POST获得的密码是加密一次的,需要调用函数再进行一次加密
        return render(request,'user/user_login.html')

#商品添加到购物车
def addToCart(request):
    #根据session获得 request.session["user_id"]=user.id,进行判断用户存在不,即判断是否登录
    userid=request.session.get("user_id")
    #根据userid获得用户名
    res=UserModel.objects.filter(pk=userid)
    #存在的状态数据
    data={
        "msg":"请求成功",
        "code":200,
        "status":"ok"
    }
    if not res.exists():   #不存在
        data["msg"]="未登录,请重新登录"
        data["code"] =901
        data["status"] ="ok"
        #重定向到登录也
        #注意,ajax请求不能直接执行重定向,需要返回Json数据,根据data["code"] =901,if判断,返回到登陆的页面
        ## return redirect(reverse("axf:logoUser"))
        return JsonResponse(data)

    user = res.first()
    #获得商品信息
    goodid=request.GET.get("goodid")
    #根据商品id查询出商品
    good=marketGoods.objects.filter(pk=goodid).first()
    #根据用户和商品查询出购物车记录,注意存在和不存在的情况
    cartRes=CartModel.objects.filter(c_goods=good,c_user=user)
    if cartRes.exists():#存在该记录,表示修改,该记录
        cart=cartRes.first()
        # cart=CartModel()
        cart.c_num +=1
        cart.save()
        data["num"]= cart.c_num
    else:           #不存在,则需要添加一条记录
        cart = CartModel()
        cart.c_goods=good
        cart.c_user=user
        cart.c_num=1
        cart.save()
        data["num"] = 1
    return JsonResponse(data)

#商品从购物车减少
def subToCart(request):

    #获得session,得到userid
    userid=request.session.get("user_id")
    #根据userid获得user
    res=UserModel.objects.filter(pk=userid)
    #user存在的状态
    data = {
        "msg": "请求成功",
        "code": 200,
        "status": "ok"
    }
    #如果user不存在,返回接送数据,根据返回的数据判断,回到登录面
    #注意ajax请求,不能进行重定向操作,需要返回json数据,在js里面进行返回登录界面
    if not res.exists():
        data["msg"] = "未登录,请重新登录"
        data["code"] = 901
        data["status"] = "ok"
        return JsonResponse(data)
    user=res.first()
    goodid=request.GET.get("goodid")
    good=marketGoods.objects.filter(pk=goodid).first()
    cart=CartModel.objects.filter(c_goods=good,c_user=user).first()
    #注意加减的两种写法
    #这个对象存在
    if cart:
        #需要判断当前数量为1的时候,为1减少一个,该记录从购物车删除
        if cart.c_num ==1:
            # print(22222222)
            # cart=CartModel()
            cart.delete()
            data["msg"] = "未登录,请重新登录"
            data["code"] = 200
            data["status"] = "ok"
            data["num"]=0
        else:
            # print(33333333333333)
            # cart = CartModel()
            cart.c_num -=1
            cart.save()
            data["code"] = 200
            data["num"] = cart.c_num
    else:#没有购物车记录
        data["msg"] = "没有该购物车记录"
        data["code"] = 902
        data["status"] = "ok"

    return JsonResponse(data)

def changeSelectStatus(request):
    data={}
    #请求获得cartid
    cartid=request.GET.get("cartid")
    cart=CartModel.objects.filter(pk=cartid).first()
    # cart=CartModel()
    cart.c_isselect= not cart.c_isselect
    cart.save()
    data["code"]="200"
    data["isselect"]=cart.c_isselect

    #设置全选是否选中
    #先判断用户是否已经登录,未登录跳转到登录页面
    userid=request.session.get("user_id")
    res=UserModel.objects.filter(pk=userid)
    if not res.exists():
        return redirect(request,reverse("axf:logoUser"))
    #根据用户查询所有的购物车记录
    user=res.first()
    carts=CartModel.objects.filter(c_user=user)

    is_allselect=True

    for cart in carts:
        # cart=CartModel()
        if not cart.c_isselect:
            is_allselect = False
            break
    data["is_allselect"]=is_allselect

    return JsonResponse(data)



def addCartNum(request):
    data={}
    cartid=int(request.GET.get("cartid"))
    cart=CartModel.objects.filter(pk=cartid).first()
    # cart=CartModel()
    cart.c_num +=1
    cart.save()
    data["code"]="200"
    data["num"]=cart.c_num

    return  JsonResponse(data)

def subCartNum(request):
    data={}
    cartid=request.GET.get("cartid")
    # print(cartid)
    cart = CartModel.objects.filter(pk=cartid).first()
    # cart=CartModel()
    # print(cart.c_num)
    if cart.c_num ==1 :
        cart.delete()
        data["code"]="901"
    else:
        cart.c_num -=1
        cart.save()
        data["code"] = "200"
        data["num"] = cart.c_num

    return JsonResponse(data)


def chanageCartSelect(request):
    print("刚进来")
    data={}
    action=request.GET.get("action")
    #action是字符串类型
    print(action)
    print(type(action))
    if action == "0":
        print(222222222)
        isselectList = request.GET.get("isselectList").split("#")
        print(isselectList)
        for cartid in isselectList:
            # print(cartid)
            print(type(cartid))     #注意是字符串的类型
            cartid=int(cartid)
            #根据id找到购物车里的
            cart=CartModel.objects.filter(pk=cartid).first()
            # cart=CartModel()
            #此时为全选状态,将属性置为Flase
            cart.c_isselect = False
            cart.save()
            data["code"]="200"
            data["msg"] = "取消全选成功"
    elif action == "1":
        #找出未选中的状态,将未选中的都置为选中状态
        noselectList = request.GET.get("noselectList").split("#")
        print(123)
        print(noselectList)
        for cartid in noselectList:
            cartid=int(cartid)
            cart=CartModel.objects.filter(pk=cartid).first()
            # cart=CartModel()
            cart.c_isselect=True
            cart.save()
            data["code"]="200"
            data["msg"] = "全选成功"
    return  JsonResponse(data)

#点击选好了生成一个订单
def generateOrder(request):
    data={}
    isSelect=request.GET.get("isSelect").split("#")
    # print(11)
    # print(isSelect)
    userid=request.session.get("user_id")
    # print(type(userid))
    user=UserModel.objects.filter(pk=userid).first()

    order=orderModel()
    #订单号需要回传到ajax数据,
    order.o_number=str(uuid.uuid4())
    order.o_user=user
    order.o_status=1
    order.save()
    #生成一个订单商品表
    print("表里的订单号")
    print(order.o_number)
    for cartid in isSelect:

        cartid=int(cartid)
        cart=CartModel.objects.filter(pk=cartid).first()
        # cart=CartModel()
        goodsNum=cart.c_num
        goods=cart.c_goods

        orderGoods=orderGoodsModel()
        orderGoods.og_goods=goods
        orderGoods.og_number=goodsNum
        #关联订单
        orderGoods.og_order=order
        orderGoods.save()

        #生成订单后将购物车记录删除
        cart.delete()
        data["code"]="200"
        #得到订单号,返回到ajax数据中
        data["orderNumber"]=order.o_number
    return JsonResponse(data)

#订单详情
def orderInfo(request,orderNumber):
    print("hahhaha这里的订单号")
    print(orderNumber)
    #根据订单号,获得订单的信息
    order=orderModel.objects.filter(o_number=orderNumber).first()
    # order=orderModel()
    #从表查主表,查出商品信息
    ordergoods=order.ordergoodsmodel_set.all()
    print(ordergoods)

    # ordergood=orderGoodsModel()
    # ordergood.og_goods.productimg
    # ordergood.og_goods.productname

    data={
        "orderNumber":orderNumber,
        "ordergoods":ordergoods,
    }
    return render(request,"order/order_info.html",context=data)