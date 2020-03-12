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




```
for(var i = 0; i < ip.length; i++){
	if(ip[i].title.toString().match(/End/)){
		console.log(ip[i].title.toString().match(/End/).input)
    }	
}
```

```
for(var i = 0,index = 1; i < ip.length; i++){
	if(ip[i].title.toString().match(/End/)){
		console.log(ip[i].title.toString().match(/End/).input);
		console.log(index);
		index++;
    }	
}
```