from django.db import models

# Create your models here.

#主页的modle
# 父类,方便继承
class Home(models.Model):
    img=models.CharField(max_length=200)
    name=models.CharField(max_length=100)
    trackid=models.CharField(max_length=16)
#     方便关联,定义成抽象的
    class Meta:
        abstract=True

# 创建一个轮播图数据库模型
# insert into axf_wheel(img,name,trackid) values("http://img01.bqstatic.com//upload/activity/2017031716035274.jpg@90Q.jpg","酸奶女王","21870"),("http://img01.bqstatic.com//upload/activity/2017031710450787.jpg@90Q.jpg","优选圣女果","21869"),("http://img01.bqstatic.com//upload/activity/2017030714522982.jpg@90Q.jpg","伊利酸奶大放价","21862"),("http://img01.bqstatic.com//upload/activity/2017032116081698.jpg@90Q.jpg","鲜货直供－窝夫小子","21770"),("http://img01.bqstatic.com//upload/activity/2017032117283348.jpg@90Q.jpg","鲜货直供－狼博森食品","21874");

class HomeWheel(Home):

    # 指定表明
    class Meta:
        db_table='axf_wheel'

# 顶部导航模型
#insert into axf_nav(img,name,trackid) values("http://img01.bqstatic.com//upload/activity/2017032016495169.png","每日必抢","21851"),("http://img01.bqstatic.com//upload/activity/2016121920130294.png","每日签到","21753"),("http://img01.bqstatic.com//upload/activity/2017010517013925.png","鲜货直供","21749"),("http://img01.bqstatic.com//upload/activity/2017031518404137.png","鲜蜂力荐","21854");

class HomeNav(Home):

    class Meta:
        db_table='axf_nav'


#insert into axf_mustbuy(img,name,trackid) values("http://img01.bqstatic.com//upload/activity/2017031715194326.jpg@90Q.jpg","酸奶女王","21870"),("http://img01.bqstatic.com//upload/activity/cms_118826_1489742316.jpg@90Q","鲜果女王","21861"),("http://img01.bqstatic.com//upload/activity/2017031011044918.jpg@90Q.jpg","麻辣女王","21866"),("http://img01.bqstatic.com//upload/activity/2017022318314545.jpg@90Q.jpg","鲜货直供－果析","21858");

#必买产品
class HomeMustbuy(Home):

    class Meta:
        db_table='axf_mustbuy'


#insert into axf_shop(img,name,trackid) values("http://img01.bqstatic.com//upload/activity/2016121616565087.png@90Q.png","闪送超市","1464"),("http://img01.bqstatic.com//upload/activity/2017031018405396.png@90Q.png","热销榜","104749"),("http://img01.bqstatic.com//upload/activity/2017031018403438.png@90Q.png","新品尝鲜","104747"),("http://img01.bqstatic.com//upload/activity/2016121618424334.png@90Q.png","牛奶面包","103536"),("http://img01.bqstatic.com//upload/activity/2016121617150246.png@90Q.png","饮料酒水","103549"),("http://img01.bqstatic.com//upload/activity/201612161714501.png@90Q.png","优选水果","103532"),("http://img01.bqstatic.com//upload/activity/2016121618550639.png@90Q.png","更多","100001"),("http://img01.bqstatic.com//upload/activity/2017031318520359.jpg@90Q.jpg","鲜蜂力荐","21854"),("http://img01.bqstatic.com//upload/activity/2016121618233839.png@90Q.png","卤味-鸭货不能停","21742"),("http://img01.bqstatic.com//upload/activity/2016121618232773.png@90Q.png","零食轰趴","21142"),("http://img01.bqstatic.com//upload/activity/2016121618235123.png@90Q.png","整箱购","20581");
#购物类型
class HomeShop(Home):

    class Meta:
        db_table='axf_shop'


#购物产品
#insert into axf_mainshow(trackid,name,img,categoryid,brandname,img1,childcid1,productid1,longname1,price1,marketprice1,img2,childcid2,productid2,longname2,price2,marketprice2,img3,childcid3,productid3,longname3,price3,marketprice3) values("21782","优选水果","http://img01.bqstatic.com//upload/activity/2017031018205492.jpg@90Q.jpg","103532","爱鲜蜂","http://img01.bqstatic.com/upload/goods/201/701/1916/20170119164159_996462.jpg@200w_200h_90Q","103533","118824","爱鲜蜂·特小凤西瓜1.5-2.5kg/粒","25.80","25.8","http://img01.bqstatic.com/upload/goods/201/611/1617/20161116173544_219028.jpg@200w_200h_90Q","103534","116950","蜂觅·越南直采红心火龙果350-450g/盒","15.3","15.8","http://img01.bqstatic.com/upload/goods/201/701/1916/20170119164119_550363.jpg@200w_200h_90Q","103533","118826","爱鲜蜂·海南千禧果400-450g/盒","9.9","13.8");
class HomeMainshow(Home):
    categoryid=models.CharField(max_length=16)
    brandname=models.CharField(max_length=200)

    img1=models.CharField(max_length=200)
    childcid1=models.CharField(max_length=16)
    productid1=models.CharField(max_length=200)
    longname1=models.CharField(max_length=100)
    price1=models.CharField(max_length=100)
    marketprice1=models.CharField(max_length=100)

    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=16)
    productid2 = models.CharField(max_length=200)
    longname2 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=100)
    marketprice2 = models.CharField(max_length=100)

    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=16)
    productid3 = models.CharField(max_length=200)
    longname3 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=100)
    marketprice3 = models.CharField(max_length=100)

    class Meta:
        db_table='axf_mainshow'

#################################
#超市market

#商品类型模型
#insert into axf_foodtypes(typeid,typename,childtypenames,typesort) values("104749","热销榜","全部分类:0",1),("104747","新品尝鲜","全部分类:0",2),("103532","优选水果","全部分类:0#进口水果:103534#国产水果:103533",3),("103581","卤味熟食","全部分类:0",4),("103536","牛奶面包","全部分类:0#酸奶乳酸菌:103537#牛奶豆浆:103538#面包蛋糕:103540",5),("103549","饮料酒水","全部分类:0#饮用水:103550#茶饮/咖啡:103554#功能饮料:103553#酒类:103555#果汁饮料:103551#碳酸饮料:103552#整箱购:104503#植物蛋白:104489#进口饮料:103556",6),("103541","休闲零食","全部分类:0#进口零食:103547#饼干糕点:103544#膨化食品:103543#坚果炒货:103542#肉干蜜饯:103546#糖果巧克力:103545",7),("103557","方便速食","全部分类:0#方便面:103558#火腿肠卤蛋:103559#速冻面点:103562#下饭小菜:103560#罐头食品:103561#冲调饮品:103563",8),("103569","粮油调味","全部分类:0#杂粮米面油:103570#厨房调味:103571#调味酱:103572",9),("103575","生活用品","全部分类:0#个人护理:103576#纸品:103578#日常用品:103580#家居清洁:103577",10),("104958","冰激凌","全部分类:0",11);

class marketFoodtypes(models.Model):

    typeid=models.CharField(max_length=16)
    typename=models.CharField(max_length=100)
    childtypenames=models.CharField(max_length=200)
    typesort=models.CharField(max_length=100)

    class Meta:
        db_table='axf_foodtypes'

#商品分类
#insert into axf_goods(productid,productimg,productname,productlongname,isxf,pmdesc,specifics,price,marketprice,categoryid,childcid,childcidname,dealerid,storenums,productnum) values("11951","http://img01.bqstatic.com/upload/goods/000/001/1951/0000011951_63930.jpg@200w_200h_90Q","","乐吧薯片鲜虾味50.0g",0,0,"50g",2.00,2.500000,103541,103543,"膨化食品","4858",200,4);

class marketGoods(models.Model):

    productid=models.CharField(max_length=16)
    productimg=models.CharField(max_length=100)
    productname=models.CharField(max_length=200)
    productlongname=models.CharField(max_length=200)
    isxf=models.CharField(max_length=100)
    pmdesc=models.CharField(max_length=100)
    specifics=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    marketprice=models.CharField(max_length=100)
    categoryid=models.CharField(max_length=16)
    childcid=models.CharField(max_length=16)
    childcidname=models.CharField(max_length=200)
    dealerid=models.CharField(max_length=16)
    storenums=models.CharField(max_length=20)
    productnum=models.CharField(max_length=20)

    class Meta:
        db_table='axf_goods'

#用户存储信息表
class UserModel(models.Model):
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=100,unique=True)

    sex = models.BooleanField(default=1)
    #头像
    icons = models.ImageField(upload_to="icons")

#   逻辑删除
    isdelete = models.BooleanField(default=0)

    class Meta:
        db_table = "axf_usermodel"
        
#手动创建 用户 多对多 商品的关系表
class CartModel(models.Model):
    c_user=models.ForeignKey(UserModel)         #关联用户表
    c_goods=models.ForeignKey(marketGoods)      #关联商品表
    c_num=models.IntegerField(default=1)        #表示购买数量
    c_isselect=models.BooleanField(default=1)   #表示是否选中
    
    class Meta:
        db_table="axf_cartModel"

#点击选好了,生成订单
"""
订单表:
id  
o_number  订单号
o_user     用户
o_datatime   订单的创建时间
o_status   订单状态码  未付款1,待收货2,待评价3,退款/售后4

一个订单放多个商品 (此表不放商品)

商品订单表:

订单号
og_goods    购买的物品
og_num      所购买物品的数量

表关系:一个用户  多个订单
       一个订单  多个商品

"""
#订单表
class orderModel(models.Model):

    o_number=models.CharField(max_length=64)
    o_user=models.ForeignKey(UserModel)
    o_datatime=o_datatime =models.DateTimeField(auto_now=True)
    o_status=models.IntegerField(default=0)

    class Meta:
        db_table="axf_ordermodel"

#订单商品表
class orderGoodsModel(models.Model):

    og_order=models.ForeignKey(orderModel)
    og_number=models.IntegerField(default=1)
    og_goods=models.ForeignKey(marketGoods)

    class Meta:
        db_table="axf_ordergoodsmodel"