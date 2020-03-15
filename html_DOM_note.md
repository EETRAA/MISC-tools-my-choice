- [ ] 一会儿加注释
- [ ] 用导航来完成更多信息的输出，可以考虑使用图表


# DOM(Document Object Model)

## 节点以及导航

```
<p>Hello world!</p>
```

节点`<p>`中`Hello world`是其子节点，称为文本节点使用`innerHTML`属性来访问文本节点的值。

## 结构：

`对象`及其`方法`，`属性`，`事件`

## 对象

1. JS对象
2. browser对象
3. DOM对象
4. html对象

## 临时代码

```javascript
for (){
	if (element[i].childcount == 1){
		console.info(element.title)
	}
}

ip = document.getElementsByTagName("acronym")

ip[0].title

ip[0].childElementCount

ip.lenth

consol.info(ip[i].title)
```

```javascript
show_per_page = document.getElementById("xpp")

show_per_page.value = "2"

proxy_type_select = document.getElementById("xf5")

proxy_type_select.value = "2"

proxy_type_select.onchange()

show_per_page.onchange()
```




```javascript
ip = document.getElementsByTagName("acronym")

for(var i = 0,index = 1; i < ip.length; i++){
	if(ip[i].title.toString().match(/End/)){
		console.log(ip[i].title.toString().match(/End/).input);
		console.log(index);
		index++;
    }	
}
```

```javascript
ip = document.getElementsByClassName("c-input c-input-large op-ip-input")

click = document.getElementsByClassName("c-btn c-btn-primary op-ip-do-submit OP_LOG_BTN")

ip[0].value = "120.236.251.50";

click[0].click()

```

```
ip = document.getElementsByTagName("acronym")

parser = ip[5].parentElement.parentElement.parentElement.innerText.split(":",2)

parser[0]

parser[1].slice(0,parser[1].indexOf("SOCKS",0)).trim()
```
