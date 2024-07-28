document.getElementById('button').onclick = function() {
    window.location.href = 'sign.html'; 
};

window.onscroll = function() {
    var navbar = document.getElementById("navbar");
    if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
        navbar.style.top = "0";
    } else {
        navbar.style.top = "-80px";
    }
};
