// ==UserScript==
// @name         成绩定时刷新
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        http://www.zfjw.xupt.edu.cn/jwglxt/cjcx*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    /* 变量声明 */

    var button = document.getElementById('search_go')

    /* 函数声明 */

    function btn_click () {

        button.click()

        console.log('\nLast time refresh at ' + Date())//输出上次刷新的时间
    }

    /* 加载完成后运行入口 */
    window.onload=function(){

        setTimeout(execute_my_script,1)

    }
	/* 实际运行的函数 */
    function execute_my_script(){
        btn_click()
        var refresh = setInterval(btn_click,60*60*1000)

    }

    // Your code here...
})();