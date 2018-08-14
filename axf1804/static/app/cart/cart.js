$(function () {
    //点击商品前选中的勾是否选中
    $(".is_chooice").click(function () {
        // alert("点击了勾选框按钮")
        //获得cartid
        currentChooice=$(this)
        cartid=currentChooice.parents("li").attr("cartid")
        $.getJSON("/axf/changeSelectStatus",{"cartid":cartid},function (data) {
            if(data["code"]=="200"){
                if(data["isselect"]){
                    currentChooice.find("span").html("√")
                    //后续的赋值,pyhon与html中true True大小不一样
                    currentChooice.attr('is_select','True')
                }else {
                    currentChooice.find("span").html("")
                    //后续的赋值,pyhon与html中true True大小不一样
                    currentChooice.attr('is_select','False')
                }

                if (data["is_allselect"]){  //选中
                    $("#all_select").find("span").html("√")
                }else{
                    $("#all_select").find("span").html("")
                }



            }else{

            }

        })
    })

    //购物车中商品数量加事件
    $(".addCartNum").click(function () {
        // alert("点击了+++++++++")
        addCartNum=$(this)
        cartid=addCartNum.parents("li").attr("cartid")
        $.getJSON("/axf/addCartNum/",{"cartid":cartid},function (data) {
            if(data["code"]=="200"){
                addCartNum.prev().html(data["num"])
            }

        })
    })
    //购物车中商品数量减事件
    $(".subCartNum").click(function () {
        // alert("点击了----------")
        subCartNum=$(this)
        cartid=subCartNum.parents("li").attr("cartid")
        $.getJSON("/axf/subCartNum",{"cartid":cartid},function (data) {
            if(data["code"] == "200"){
                subCartNum.next().html(data["num"])
            }else if(data["code"] == "901"){
                subCartNum.parents("li").remove()
            }

        })

    })

    //全选按钮点击事件
    $("#all_select").click(function () {
        // alert("全选hahhhahahah")
        //只要有一个是未选中的点击后,所有的都为选中状态 且勾选矿打勾
        //只要有一个是选中的点击后,所有的都未选中,且勾选框不打钩
        //解决方式  客户端,服务端
        isselectList=[]
        noselectList=[]
        allselect=$(this)
        $(".is_chooice").each(function () {
            currentCh=$(this)
            isSelect=currentCh.attr("is_select")
            if(isSelect == "True"){
                //选中后将cartid装入容器
                cartid=currentCh.parents("li").attr("cartid")
                isselectList.push(cartid)
            }else{
                cartid=currentCh.parents("li").attr("cartid")
                noselectList.push(cartid)
            }
        })
        console.log(isselectList)
        console.log(noselectList)

        if(noselectList.length==0){    //当前是全部选中状态
            //其他的都为全部不选中,全选按钮框,置为不打钩状态
            $.getJSON("/axf/chanageCartSelect",{"isselectList":isselectList.join("#"),"action":0},function (data) {
                if(data["code"]=="200"){
                     $(".is_chooice").each(function () {
                     $(this).find("span").html("")
                     $(this).attr("is_select","False")
                    })
                    allselect.find("span").html("")
                }


            })

        }else{  //只要有一个未选中状态,全部置为选中状态,全选按钮框,置为打钩状态
            $.getJSON("/axf/chanageCartSelect",{"noselectList":noselectList.join("#"),"action":1},function (data) {
                if(data["code"]=="200"){
                     $(".is_chooice").each(function () {
                     $(this).find("span").html("√")
                     $(this).attr("is_select","True")
                    })
                    allselect.find("span").html("√")
                }
            })
        }
    })

    //点击选好了,生成订单
    $("#generate_order").click(function () {
        // alert("点击选好了")
        //获得选中的cartid
        isSelect=[]
        $(".is_chooice").each(function () {
            if ($(this).attr("is_select") == "True"){
                //获得id装入容器中
                isSelect.push($(this).parents("li").attr("cartid"))
            }
        })
        console.log(isSelect)

        if(isSelect.length == 0){   //没有选中商品
            alert("请选择购买的商品")
        }else{
            //ajax请求传递 cartid
            $.getJSON("/axf/generateOrder",{"isSelect":isSelect.join("#")},function (data) {
                if(data["code"]=="200"){    //生成订单成功
                    console.log(data["orderNumber"])
                    //打开订单详情
                    // window.open("/axf/orderInfo/" + data["orderNumber"],target="_self")
                    //注意携带参数时,路径后边用斜扛隔开,太坑里啊
                    window.open("/axf/orderInfo/" + data["orderNumber"],target="_self")
                }
            })

        }


    })

////
})