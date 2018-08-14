$(function () {

    //启动顶部菜单轮播
    initSwiper()
    //启动必买
    initMustbuy()
})

function initSwiper() {
    var mySwiper = new Swiper ('#topSwiper', {
        // direction: 'vertical',  垂直
        autoplay: 5000,  //可选选项,自动滑动
        loop: true,

        // 如果需要分页器
        pagination: '.swiper-pagination',
    })
}


function initMustbuy() {
    var mySwiper = new Swiper ('#swiperMenu', {
        // direction: 'vertical',  垂直
        // autoplay: 5000,  //可选选项,自动滑动
         slidesPerView: 3,      //每页的数量
         spaceBetween: 5,      //相隔间距
        // 如果需要分页器
        // pagination: '.swiper-pagination',
    })
}
