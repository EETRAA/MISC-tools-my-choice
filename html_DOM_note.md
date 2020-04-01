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

### 数组的方法

```javascript
//回调函数应当返回值，
或不返回也行（此时当做无返回的操作函数f(x)看待,f非y=f(x)）
list.forEach(callbackfunc(item,index,arr),thisValue);
//此方法将轮询一次当前数组元素，将数组的当前轮询选中元素，当前轮询选中元素的索引号，当前数组对象本身按顺序传给回调函数。原数组不受影响。

list.redecu(callbackfunc(total,item,index,arr),thisValue);
//此方法将轮询一次当前数组元素，每次执行回调函数后，将回调函数的返回值赋值给total，轮询完后返回最终的total值。
```

### let keyword

let使用方法，var声明的属于全局的变量

```javascript
let x = 1;

if (x === 1) {
  let x = 2;

  console.log(x);
  // expected output: 2
}

console.log(x);
// expected output: 1

```

同作用域内不能用let重新声明let定义的变量

```javascript
let x = 1;

if (x === 1) {
  let x = 2;
  let x = 1;//illegal
}

let x = 2;//illegal
```

for...of与for...in的区别
无论是for...in还是for...of语句都是迭代一些东西。它们之间的主要区别在于它们的迭代方式。

for...in 语句以任意顺序迭代对象的可枚举属性。

for...of 语句遍历可迭代对象定义要迭代的数据。

以下示例显示了与Array一起使用时，for...of循环和for...in循环之间的区别。

```javascript
Object.prototype.objCustom = function() {}; 
Array.prototype.arrCustom = function() {};

let iterable = [3, 5, 7];
iterable.foo = 'hello';

for (let i in iterable) {
  console.log(i); // logs 0, 1, 2, "foo", "arrCustom", "objCustom"
}

for (let i in iterable) {
  if (iterable.hasOwnProperty(i)) {
    console.log(i); // logs 0, 1, 2, "foo"
  }
}

for (let i of iterable) {
  console.log(i); // logs 3, 5, 7
}
```
### JSON数据格式解析

json中，始终将 `{}` 里的东西当做对象，**始终遵循上一级为对象，下一级为属性的原则**来构建json数据

json不能注释

- 如 `object = {}` 则 `{}` 中为 `object` 的属性
- 如 `{"obejct":{}}` 则 `object` 为上一级的属性，对于下一级来说为下一级的对象

1. json对象数组

```json
{
"sites": [										//当sites为对象时，{"sites":[{},{},{}]}
{ "name":"google1" , "url":"www.google.com" }, 	//这是第一个对象，sites[0]，大括号内含有属性，访问方式sites[0].name/url
{ "name":"google2" , "url":"www.google.com" }, 	//这是第二个对象，sites[1]……
{ "name":"google3" , "url":"www.google.com" }	//这是第三个对象，sites[2]……
]
}
```

2. json嵌套

```json
{
	"Object":{
		"name":"google",
		"alexa":"1",
		"sites":{						//单对象嵌套，访问方式Object.sites.site1/2/3
			"site1":"www.google.com",
			"site2":"www.google.com",
			"site3":"www.google.com"
		},
		"sites_duplicate":[				//多对象嵌套，访问方式Object.sites[0].site1
		{"site1":"www.google.com"},
		{"site2":"www.google.com"},
		{"site3":"www.google.com"}
		]
	}
}
```

3. json使用js语法

```javascript
	Object = {
		"name":"google",
		"alexa":"1",
		"sites":{
			"site1":"www.google.com",
			"site2":"www.google.com",
			"site3":"www.google.com"
		}
	}
```

### js定时器

```javascript

function console_log(content){
	console.log(content);
}

TimerA = setInterval("console_log('hi, there!')",1000);	//字符串有参传入函数

TimerA = setInterval("console_log()",1000);				//字符串无参传入函数

TimerA = setInterval(console_log,1000);					//handler方式传入函数

clearInterval(TimerA)

```

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

temp[0].placeholder;//输出为其内置属性，此处为ip
temp[1].placeholder;//输出为其内置属性，此处为port

```

document.getElementById

document.getElementsByName

document.getElementsByTagName

document.getElementsByClassName

都是实时的，文档有更新会自动更新。

document.querySelector(css选择器)

dcument.querySelectorAll(css选择器)

非实时

### 待更新代码

```javascript
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

```
