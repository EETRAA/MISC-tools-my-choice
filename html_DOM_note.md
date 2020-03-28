loca = document.getElementsByClassName("ng-binding ng-isolate-scope");//获取左边代理栏元素

loca[0].click();//初始化的第一个代理项目

function show_ip_n_port(){
	temp = document.querySelectorAll("input[placeholder]");//选择返回为一个列表，选择方式为CSS选择器
	console.log(temp[0].placeholder);
	console.log(temp[1].placeholder);
	
	}

for(i=0;i<(loca.length-2);i++){
	
	//console.log(document.readyState);
	
    console.log(loca[i].innerText);//显示当前代理名

    loca[i].click();//选中当前代理

    //使用window.onload，当页面没加载好就不执行，会跳过此段代码
	//setTimeout(show_ip_n_port,2000);其中function_handler并不会当时立即执行，而是真的在延时后执行。如有多个则会在之后一并执行。
	
}
