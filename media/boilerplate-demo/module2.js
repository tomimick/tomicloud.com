// module2.js
var MODULE2 = (function () {

    // variables and functions private unless attached to API below
    // 'this' refers to global window

    // initialize this module
    function init() {
        MAIN.log("module2.js loaded");

        // append 2 links
        $("#load2").remove();
        $("#box2")
            .append("<a href='#'>jQuery plugin, instance 1</a>")
            .append("<a href='#'>jQuery plugin, instance 2</a>");

        // attach my jquery plugin to 1st link
        $("#box2 > a:first").myplugin();

        // attach my jquery plugin to 2st link with options
        var options = {msg : "Boom!"};
        $("#box2 > a:last").myplugin(options);

        // get the API to the plugin object
        // var obj = $('#elem').data('myplugin');
        // api.change_msg("Hello there!");
    }

    // public and private functions of the module here...
    // ...


    // define the public API
    var API = {};
    API.init = init;

    return API;
}());

