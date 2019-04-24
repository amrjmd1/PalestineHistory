$(function () {
    var circle = $('.my-progress .circle'),
        glPers = 0,
        day = new Date(),
        // day = newDate('2018, 3,1'),
        // day = newDate('2018, 2, 28'),
        startDay = newDate($('.circle').first().data('date')),
        endDay = newDate($('.circle').last().data('date')),
        countAllDAy = differenceDays(startDay, endDay),
        fillDay = 100 - ((100 / countAllDAy) * (differenceDays(day, endDay))),
        allActive = [],
        monthNames = [" يناير", "فبراير", "مارس", "ابريل", "مايو", "يونيو", "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"];
    // monthNames = [" كانون الثاني", "شباط", "آذار", "نيسان", "أيار", "حزيران", "تموز", "آب", "أيلول", "تشرين الأول", "تشرين الثاني", "كانون الأول"];
    $('#active-carousel').carousel({interval: false})

    $('.my-progress .fill').tooltip({
        html: true,
        title: "<span class='title'>اليوم الحالي</span><span class='date'>*</span>".replace('*', day.getDate() + ' ' + monthNames[day.getMonth()] + ' ' + day.getFullYear())
    });

    function differenceDays(fDay, eDay) {
        return Math.ceil((eDay - fDay) / (1000 * 60 * 60 * 24))
    }

    function newDate(date) {
        var time = date.split(',')
        return new Date(parseInt(time[0]), (parseInt(time[1]) - 1), parseInt(time[2]))
    }

    circle.each(function () {
        var thisDay = newDate($(this).data('date')),
            title = "<span class='title'>X</span><span class='date'>*</span>";
        title = title.replace('*', thisDay.getDate()) + ' ' + monthNames[thisDay.getMonth()] + ' ' + thisDay.getFullYear();
        title = title.replace('X', $(this).data('title'))
        $(this).tooltip({
            html: true,
            title: title
        })
        if ($(this).index() != $(this).siblings().length - 1) {
            var diff = differenceDays(newDate($(this).data('date')), newDate($(this).next().data('date'))),
                pers = (100 / countAllDAy) * diff;
            $(this).css('right', glPers + '%');
            if (glPers <= fillDay) {
                allActive.push([$(this)])
                $(this).removeClass('active-now').addClass('active-check').html('<i class="fa fa-check"></i>')
            }
            glPers += pers;
        } else {
            $(this).css('right', '100%')
            if (differenceDays(day, endDay) <= 0) {
                allActive = []
                $(this).addClass('active-now').siblings().removeClass('active-now')
                $('#face-0'.replace('0', $(this).data('count'))).addClass('active')
            }
        }
    });
    if (allActive.length) {
        var activeNow = allActive[allActive.length - 1][0];
        activeNow.removeClass('active-check').addClass('active-now').html(activeNow.data('count'))
        $('#face-0'.replace('0', activeNow.data('count'))).addClass('active')
    }
    if (fillDay < 100) {
        $('.my-progress .fill').css('width', fillDay + '%')
    }
});