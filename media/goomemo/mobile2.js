
/* simple mobile browser detection */

function main() {
    if (ismobile()) {
        document.body.className = "mob";
    } else {
        document.body.className = "big";
    }
}

function ismobile() {
    var agent = navigator.userAgent;
    if (/Android/.test(agent) || /iPhone/.test(agent) || /Symbian/.test(agent))
        return true;

    return false;
}

if (window.addEventListener)
    window.addEventListener('load', main, false);
else
    window.attachEvent('onload', main);

