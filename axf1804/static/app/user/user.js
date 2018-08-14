$(function () {
    //验证密码是否一致
    //确认的密码框设置一个内容改变事件
    $("#confirm_pwd").change(function () {

        //获取到输入框中的值
        pwd1=$("#pwd").val()
        pwd2=$("#confirm_pwd").val()


        if(pwd1 == pwd2){
            //密码相同提示一致
            $("#message").html('两次密码一致')
            $("#message").css('color','green')
        }else{
            //密码不同提示不一致
            $("#message").html('两次密码不一致,请重新输入')
            $("#message").css('color','red')
        }
    })

    //监听用户名输入框的改变,确认用户名是否已存在,已存在不能使用  注意不能使用的生命,让他返回false不能注册,
    //可以利用$("#username_info").html(data["msg"]).css("color","rgb(0,255,0)")的属性进行判断
    $("#username").change(function () {
        // alert(data)
        // alert("用户")
        // ajax请求服务器
        myusername=$(this).val()
        $.getJSON("/axf/checkUser",{"username":myusername},function (data) {
            console.log(data)

            if(data["code"] == "200"){ //用户名可以使用
                $("#username_info").html(data["msg"]).css("color","rgb(0,255,0)")

            }else if(data["code"] == "901"){
                $("#username_info").html(data["msg"]).css("color","rgb(255,0,0)")
            }


        })

    })


})

//验证输入的内容合法
//合法返回True
//不合法返回False,表示不可以提交
function check_input() {
    //合法判断
    //1,用户名没有被注册---请求服务器判断
    //2,密码长度大于6,合法的字符
    //3,密码与确认密码必须一致
    //4,提交md5处理后的
    pwd1=$("#pwd").val()
    pwd2=$("#confirm_pwd").val()

    //对用户名是否已存在,进行判断给出返回值
    color=$("#username_info").attr("color")
    if(color == "rgb(255,0,0)"){
        return false
    }

    if(pwd1.length < 6 ){
        //提示密码长度不够
        return false
    }

    if(pwd1 != pwd2){
        //提示两次密码不一致
        return false
    }

    //将加密后的结果设置到密码输入框中去
    result=md5(pwd1)

    // alert(result)

    $("#pwd").val(result)

    // alert(pwd1)

    return true

}