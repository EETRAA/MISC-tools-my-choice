// ==UserScript==
// @name         download_video
// @namespace    http://N/A.net/
// @version      0.1
// @description  try to take over the world!
// @author       E.T.R.A
// @match        http://e-learning.d.wcsapi.biz.matocloud.com/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    // Your code here...
	/* 变量声明 */

    var eleLink
    var b

	/* 函数声明 */

    function download_video () {

        /* 获取当前视频元素 */
        b = document.getElementsByTagName("source")
        /* 选择视频元素 */
        b[0].getAttribute('src')

        /* 下载视频 */
        var eleLink = document.createElement('a');
        eleLink.download = b[0].getAttribute('src')
        eleLink.style.display = 'none';
        /* 字符内容转变成blob地址 */
        eleLink.href = b[0].getAttribute('src')
        /* 触发点击 */
        document.body.appendChild(eleLink);
        eleLink.click();
        /* 然后移除 */
        document.body.removeChild(eleLink);

    }


	/* 加载完成后运行入口 */
    window.onload=function(){

        setTimeout(execute_my_script,1)

    }
	/* 实际运行的函数 */
    function execute_my_script(){

        download_video()
        window.close()

    }
})();