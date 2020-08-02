// ==UserScript==
// @name         Sangfor college auto play
// @namespace    http://N/A.net/
// @version      0.1
// @description  try to take over the world!
// @author       E.T.R.A
// @match        http://college.sangfor.com/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    // Your code here...
	/* 变量声明 */
    var btn_next = document.querySelector('.btn.btn-default.js-next-mobile-btn')
	/* 函数声明 */
    function btn_next_click () {
        btn_next.click()

    }


	/* 加载完成后运行入口 */
    window.onload=function(){

        setTimeout(execute_my_script,2000)

    }
	/* 实际运行的函数 */
    function execute_my_script(){

        setTimeout(btn_next_click,20*60*1000)

    }
})();