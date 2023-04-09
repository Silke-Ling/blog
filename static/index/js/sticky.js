window.onscroll=function()
{
    var tag = document.getElementById("sticky"); //获取标签id
    var height=50                              //高度定位设置
    //当滚动距离大于高度定位时sticky
    if(window.pageYOffset>=document.documentElement.clientHeight-height)
    { 
        tag.style.position = 'fixed';
        tag.style.top='0%';       
        //bignav.style.zIndex = '9999';
    }
    //当滚动距离小于高度定位时，让导航栏恢复原状
    else{
        tag.style.position = 'absolute';
        tag.style.top=null;
        tag.style.bottom = '0%';
    }
}