- [x] 一会儿加注释
- [x] 用导航来完成更多信息的输出，~~可以考虑使用图表~~


# DOM(Document Object Model)

## 节点以及导航

```
<p>Hello world!</p>
```

节点 `<p>` 中 `Hello world` 是其子节点，称为文本节点使用 `innerHTML` 属性来访问文本节点的值。

## 结构：

`对象` 及其 `方法`，`属性`，`事件`

## 对象

1. JS对象
2. browser对象
3. DOM对象
4. html对象

## js笔记

- `rototype` 属性使您有能力向对象添加属性和方法。

- 当构建一个属性，所有的数组将被设置属性，它是默认值。

- 在构建一个方法时，所有的数组都可以使用该方法。

## 正式代码

### 修改页面显示的类型和每页显示数量

```javascript

function Show_100_Type_socks() {
	
	show_per_page = document.getElementById("xpp");

	show_per_page.value = "2";

	proxy_type_select = document.getElementById("xf5");

	proxy_type_select.value = "2";

	proxy_type_select.onchange();

	show_per_page.onchange();
	
    return "successfully done";
}

```

### 解析页面，获取页面的EndIP信息并输出至控制台

```javascript

function IP_parser() {
	
	ip = document.getElementsByTagName("acronym");//获取页面上含EndIP的元素，注意有时候重复

	for(var i = 0,index = 1; i < ip.length; i++){
		
		if(ip[i].title.toString().match(/End/)){//如果RE匹配成功，也就是此元素存在
		
			console.log(index);//标号输出
			index++;
			//以下为:原ip的初步获取-->原ip的地址获取-->原ip的端口获取
			Original_IP_Not_Sorted = ip[i].parentElement.parentElement.parentElement.innerText.split(":",2);//三次父元素巡航，找到innerText，也就是其中的文本类字符串并以“:”冒号初步分割ip地址。
			Original_IP = Original_IP_Not_Sorted[0].trim();//原ip获取
			Original_IP_Port = Original_IP_Not_Sorted[1].slice(0,Original_IP_Not_Sorted[1].indexOf("SOCKS",0)).trim();//找到初步解析的原ip端口并两端去空白
			//以下为数据的输出
			console.log("Original IP:" + Original_IP + ":" + Original_IP_Port);
			console.log(ip[i].title.toString().match(/End/).input);//则输出成功匹配的元素的值，此处是EndIP
			
		}	
	}
	return "successfully done";
}

```

## 临时代码

### 输出跳板的ip

```javascript
ip = document.getElementsByTagName("acronym")

parser = ip[5].parentElement.parentElement.parentElement.innerText.split(":",2)

parser[0]

parser[1].slice(0,parser[1].indexOf("SOCKS",0)).trim()
```

### 百度ip查询页面输入并查询代码

```javascript
ip = document.getElementsByClassName("c-input c-input-large op-ip-input");

click = document.getElementsByClassName("c-btn c-btn-primary op-ip-do-submit OP_LOG_BTN");

ip[0].value = "120.236.251.50";

click[0].click();

```

### 嵌入新的网页

```javascript
baidu = document.createElement("iframe");

baidu.setAttribute("src","https://www.baidu.com");

document.body.append(baidu);

baidu.height = 800;
baidu.width = 600;
```

1. 父级页面获取iframe页面中的元素对象（关键contentWindow）：

	`document.getElementById(iframe的id).contentWindow.document.getElementById(iframe页面元素id)`

2. iframe页面获取父级页面的元素对象（关键window.parent）：

	`window.parent.document.getElementById(父级页面的元素id)`
	
3. 需要使用 `window.onload` 来确保加载完毕

### switchyomega界面

```javascript
loca = document.getElementsByClassName("ng-binding ng-isolate-scope");

loca[0].innerText;

loca[0].click();

temp = document.querySelectorAll("input[placeholder]");//选择返回为一个列表，选择方式为CSS选择器

temp.placeholder;//输出为其内置属性
```

document.getElementById

document.getElementsByName

document.getElementsByTagName

document.getElementsByClassName

都是实时的，文档有更新会自动更新。

document.querySelector(css选择器)

dcument.querySelectorAll(css选择器)

非实时

### 数组的方法

```javascript
//回调函数应当返回值
list.forEach(callbackfunc(item,index,arr),thisValue);
//此方法将轮询一次当前数组元素，将数组的当前轮询选中元素，当前轮询选中元素的索引号，当前数组对象本身按顺序传给回调函数。原数组不受影响。

list.redecu(callbackfunc(total,item,index,arr),thisValue);
//此方法将轮询一次当前数组元素，每次执行回调函数后，将回调函数的返回值赋值给total，轮询完后返回最终的total值。
```
