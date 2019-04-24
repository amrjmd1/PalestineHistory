$(function () {
	console.log('%c       ', 'font-size: 100px; background: url(https://b.top4top.net/p_939czr051.png) no-repeat;');
    $('.fixed-menu .fixed-menu-show').click(function () {
        fixed_menu($(this));
    });
    $('.my-datedropper').dateDropper();

    fixed_menu($('.fixed-menu .fixed-menu-show'));

    function fixed_menu(fi) {
        var parent_fixed = fi.parent('.fixed-menu');
        if (!parent_fixed.hasClass('is-visible')) {
            fi.children('i').css('transform', 'rotate(0deg)');
            parent_fixed.animate({
                right: 0
            }, 800);
            $('body').animate({
                paddingRight: fi.parent('.fixed-menu').innerWidth() + 'px'
            }, 800)
        } else {
            fi.children('i').css('transform', 'rotate(180deg)');
            parent_fixed.animate({
                right: '-' + fi.parent('.fixed-menu').innerWidth() + 'px'
            }, 800);
            $('body').animate({
                paddingRight: 0
            }, 800)
        }
        parent_fixed.toggleClass('is-visible')
    }

    $(".collapse_fixed").click(function () {
        $(this).children('i').hasClass('fa-plus') ? $(this).children('i').removeClass('fa-plus').addClass('fa-minus') : $(this).children('i').removeClass('fa-minus').addClass('fa-plus');
    });
});
