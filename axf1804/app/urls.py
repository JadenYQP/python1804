from django.conf.urls import url
from django.contrib import admin

from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^home/',views.home,name='home'),

    url(r'^market/$',views.market,name='market'),
    url(r'^market/(\d+)/(\d+)/(\d+)',views.market_with_param,name='marketWP'),

    url(r'^cart/',views.cart,name='cart'),

    url(r'^mine/',views.mine,name='mine'),

    url(r'^register/',views.register,name='register'),  #注册界面

    url(r'^logout/',views.logout,name='logout'), #退出

    url(r'^checkUser/',views.checkUser,name='checkUser'), #用户确认

    url(r'^logoUser/',views.logoUser,name='logoUser'), #用户登录

    url(r'^addToCart/',views.addToCart,name='addToCart'), #商品添加

    url(r'^subToCart/',views.subToCart,name='subToCart'), #商品减少

    url(r'^changeSelectStatus/',views.changeSelectStatus,name='changeSelectStatus'), #勾选按钮点击事件

    url(r'^addCartNum/',views.addCartNum,name='addCartNum'), #cart加商品

    url(r'^subCartNum/',views.subCartNum,name='subCartNum'), #cart减商品

    url(r'^chanageCartSelect/',views.chanageCartSelect,name='chanageCartSelect'), #全选状态置为不选中状态

    url(r'^generateOrder/',views.generateOrder,name='generateOrder'), #生成订单,和商品订单表

    url(r'^orderInfo/(.+)',views.orderInfo,name='orderInfo'), #订单详情


]
