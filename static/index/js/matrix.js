var matrix=document.getElementById("matrix");
matrix.width=window.innerWidth;
matrix.height=window.innerHeight;
var columns=matrix.width/font_size;     //列数

window.onresize=resizeCanvas;
function resizeCanvas(){
    matrix.width=document.documentElement.clientWidth;
    matrix.height=document.documentElement.clientHeight;
    columns=matrix.width/font_size;     //列数

    for(var i=0;i<columns;i++)
  	    drop[i]=1;
}

var drop=[];
var font_size=16;
var context=matrix.getContext("2d");            //创建2d对象

resizeCanvas(); 

function get_random_color()             //获取随机颜色
{
    var color="#";
    for(var i=0;i<6;i++)
		color += (Math.random()*16 | 0).toString(16);       //以16进制随机表示颜色
    return color;
}
 
function drawMatrix()
{  

    context.fillStyle="rgba(0, 0, 0, 0.1)";             //填充样式设置背景color为黑色,并设置透明度为0.1
    context.fillRect(0,0,matrix.width,matrix.height);   //绘制已填色的矩形
  
    context.fillStyle=get_random_color();   //颜色变化
    context.font=font_size+"px";            //字体大小
    for(var i=0;i<columns;i++)
    {
        context.fillText(Math.floor(Math.random()*10),i*font_size,drop[i]*font_size);/*get 0 and 10*/
  
        if(drop[i]*font_size>(matrix.height*2/3)&&Math.random()>0.9)/*reset*/
	        drop[i]=0;
        drop[i]++;
    }
}
setInterval(drawMatrix,40);

