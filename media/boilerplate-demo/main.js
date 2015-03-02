// main.js
var MAIN = (function () {

    // variables and functions private unless attached to API below
    // 'this' refers to global window

    // private array
    var array = [];


    // initialize this module
    function init() {
        log("main.js loaded");

        $("#a1").click(function(){
            // add random number to array and print array
            add(rand(100));
            var a = get_array();
            log("Array: "+a.join(", "));
            return false;
        });

        $("#load2").click(function(){
            // load module2.js, module2.css and jquery plugin

            // load css separately (finish callback is not reliable with css)
            head.js("module2.css");

            // and then load js
            head.js("module2.js", "jquery-plugin.js", function(){
                MODULE2.init();
            });

            return false;
        });
    }

    // a private debug function
    function log(msg) {
        console.debug(msg);
        $("#debug").append("<p>"+msg+"</p>");
    }


    // PRIVATE functions below

    // add a number into array
    function add(a) {
        array.push(a);
    }

    // return copy of the array
    function get_array() {
        return array.slice();
    }

    // return random integer between 0-maxnum
    function rand(maxnum) {
        return parseInt(Math.random()*maxnum);
    }


    // define the public API
    var API = {};
    API.init = init;
    API.log = log;

    return API;
}());

