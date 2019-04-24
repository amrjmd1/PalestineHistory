$(function () {
    var navMain = $(".navbar-collapse");
    navMain.on("click", "a:not([data-toggle])", null, function () {
        navMain.collapse('hide');
    });
    // scrolling();
    // $(window).scroll(function () {
    //     scrolling();
    // });
    // $("#go-to-down").click(function () {
    //     $('html,body').animate({scrollTop: $(".my-nav").innerHeight() - 55}, 800);
    // });
    // $("#go-to-up").click(function () {
    //     $('html,body').animate({scrollTop: 0}, 800);
    // });

    $('.main-gallery').flickity({
        cellAlign: 'left',
        contain: true
    });
    $('#fullpage').fullpage({
        autoScrolling: true,
        scrollHorizontally: false,
        navigation: true,
        licenseKey: 'OPEN-SOURCE-GPLV3-LICENSE',
        menu: '#menu-sections',
        sectionsColor: [
            'none',
            '#60a3bc',
            '#95a5a6',
            '#fa983a',
            '#0a3d62',
            '#2d3436'
        ],
        anchors: [
            'firstPage',
            'secondPage',
            'thirdPage',
            'fourthPage',
            'fifthPage',
            'sixthPage',
        ],
    });
    $.fn.fullpage.setAllowScrolling(true);
})

function scrolling() {
    var scrollingTop = $(window).scrollTop(),
        heightHeader = $(".my-nav").innerHeight() - 56,
        percentHeight = (scrollingTop / heightHeader * 100) / 100;
    if (percentHeight <= 1) {
        $(".backgraound-nav").css("background", "rgba(2,204,186,*)".replace("*", percentHeight));
        $("#go-to-up").fadeOut();
    }
    else {
        $(".backgraound-nav").css("background", "rgba(2,204,186,1)");
        $("#go-to-up").fadeIn();
    }
}
