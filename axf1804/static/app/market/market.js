$(function () {

    $("#type_container").hide()
    $("#allsortrule").hide()

    //全部分类
    $("#allType").click(function () {
        // alert(1234)
        $("#type_container").show()
        $("#allType_g").removeClass().addClass("glyphicon glyphicon-chevron-up")

        $("#allsortrule").hide()
        $("#allsort_g").removeClass().addClass("glyphicon glyphicon-chevron-down")

    })

    //点击div菜单隐藏
    $("#type_container").click(function () {
        // alert(1234)
        $("#type_container").hide()
        $("#allType_g").removeClass().addClass("glyphicon glyphicon-chevron-down")

    })


    //全部排序
    $("#allsort").click(function () {
        // alert(1234)
        $("#allsortrule").show()
        $("#allsort_g").removeClass().addClass("glyphicon glyphicon-chevron-up")

        $("#type_container").hide()
        $("#allType_g").removeClass().addClass("glyphicon glyphicon-chevron-down")

    })

    $("#allsortrule").click(function () {
        // alert(1234)
        $("#allsortrule").hide()
        $("#allsort_g").removeClass().addClass("glyphicon glyphicon-chevron-down")

    })

//加商品点击事件
    $(".addShopping").click(function () {
        //ajax请求
        // alert("+++++++++++++++")
        //注意ajax请求中addele=$(this)必须单独拿出来用
        addele=$(this)
        goodid=addele.attr("goodid")
        // console.log(goodid+"11111")

        $.getJSON("/axf/addToCart/",{"goodid":goodid},function (data) {
            if(data["code"] == "901"){//不存在,跳转到登录页面
                window.open("/axf/logoUser",target="_self")

            }else if(data["code"] == "200"){ //添加购物车成功
                console.log(data["num"])
                //添加成功后,更新span的数量
                addele.prev().html(data["num"])

            }
        })

    })

    //减少商品点击事件
    $(".subShopping").click(function () {
        // alert("点击了-------------")
        subele=$(this)
        gooid=subele.attr("goodid")
        $.getJSON("/axf/subToCart/",{"goodid":goodid},function (data) {
            if(data["code"] == 901){
                window.open("/axf/logoUser",target="_self")

            } else if(data["code"] == 200){
                subele.next().html(data["num"])
            }

        })
    })



//
})