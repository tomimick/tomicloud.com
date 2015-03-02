
/* My blog javascript */


var MAIN = (function () {

    function main() {

    // show/hide cases
    $("#worktags a").click(function() {

        var t = $(this);
        $("#worktags a").removeClass("sel");
        t.addClass("sel");
        var cls = t.attr("data-cls");
        var cases = $(".case");
        cases.hide();
        var count = 0;
        if (cls) {
            cases.each(function(){
                var div = $(this);
                var cls2 = div.attr("data-cls");
                if (cls2.indexOf(cls)>=0) {
                    div.fadeIn();
                    count += 1;
                }
//                else
//                    div.fadeOut();
            });
        } else {
            // show all
            cases.fadeIn();
            count = cases.length;
        }
        var s = " ("+count+")";
        $("#workcount").text(s).show();

        return false;
    });

    if (window.postinit)
        postinit();

    $("img.w100, img.w50, img.w30").click(function() {
        $(this).toggleClass("big");
        return false;
    });

//    $(".nav a").click(function() {
//        $(this).toggleClass("sel");
//        return false;
//    });

//    alert("a"+ismobile());
}

    function ismobile() {
        return document.getElementById("footermob") !== null;
    }

    var API = {};
    API.main = main;

    return API;
}());

