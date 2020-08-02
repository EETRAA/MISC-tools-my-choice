// ==UserScript==
// @name         parse_video_url
// @namespace    http://N/A.net/
// @version      0.1
// @description  try to take over the world!
// @author       E.T.R.A
// @match        http://college.sangfor.com/course/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    // Your code here...
	/* 变量声明 */
    var a
	/* 函数声明 */
    function parse_video_url(){

        a = document.getElementById("lesson-video-content")

        window.open(a.getAttribute("data-url"))

    }


	/* 加载完成后运行入口 */
    window.onload=function(){

        setTimeout(execute_my_script,1)

    }
	/* 实际运行的函数 */
    function execute_my_script(){

        parse_video_url()

    }
})();