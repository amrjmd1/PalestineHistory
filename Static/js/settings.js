$(".list-type3 li a").click(function (ev) {
    var id_div = $(this).data("id");
    $('.list-type3 li a').removeClass('active_li');
    $(this).addClass('active_li');
    $('.settings_div').hide();
    $('.container').find('.div_' + id_div).fadeIn('slow');

});
$(function () {
    $(".mat-input").each(function () {
        if ($(this).val() !== "")
            $(this).parent().addClass("is-active is-completed");
    });
    setTimeout(function () {
        $("#parent_loader").css('display', 'none');
        $("body").css('overflow', 'visible');
    }, 1000);
});

$(".mat-input").focus(function () {
    $(this).parent().addClass("is-active is-completed");
});

$(".mat-input").focusout(function () {
    if ($(this).val() === "") {
        $(this).parent().removeClass("is-completed");
        $(this).parent().removeClass("is-active");
    }
});

function swal_settings(type, title) {
    swal({
        type: type,
        html: title,
        showConfirmButton: false,
        allowOutsideClick: false,
        timer: 2500
    });
}

$("#Save_Settings_Submit").click(function (ev) {
    $("#parent_loader").css('display', 'block');
    ev.preventDefault();
    $.ajax({
        type: "POST",
        url: $("meta[property='save_settings']").attr('content'),
        data: $('#Save_Settings_Form').serialize(),
        success: function (data) {
            $("#parent_loader").css('display', 'none');
            if (data.msg === "NotActive") {
                location.reload();
            } else if (data.msg === "isEmpty") {
                swal_settings('error', 'الرجاء إدخال جميع البيانات');
            } else if (data.msg === "GenderContextError") {
                swal_settings('error', 'تأكد من حقل تحديد الجنس');
            } else if (data.msg === "PhoneContextError") {
                swal_settings('error', 'تأكد من إدخال الهاتف بالصيغة الصحيحة');
            } else if (data.msg === "IdentityContextError") {
                swal_settings('error', 'تأكد من إدخال رقم هويتك بشكل صحيح');
            } else if (data.msg === "CategoryContextError") {
                swal_settings('error', 'تأكد من تحديد الفئة بشكل صحيح');
            } else if (data.msg === "Done") {
                swal_settings('success', 'تمت العملية بنجاح');
                setTimeout(function () {
                    location.reload();
                }, 2500);
            } else if (data.msg === "Fail") {
                swal_settings('error', 'عذراً، فشلت العملية');
            } else if (data.msg === "NameContextError") {
                swal_settings('error', 'لا يمكن أن يحتوي الاسم على أرقام أو رموز');
            }
        }
    });
    return false;
});

$("#Change_Email_Submit").click(function (ev) {
    $("#parent_loader").css('display', 'block');
    ev.preventDefault();
    $.ajax({
        type: "POST",
        url: $("meta[property='change_email']").attr('content'),
        data: $('#Change_Email_Form').serialize(),
        success: function (data) {
            $("#parent_loader").css('display', 'none');
            if (data.msg === "NotActive") {
                location.reload();
            } else if (data.msg === "isEmpty") {
                swal_settings('error', 'الرجاء إدخال جميع البيانات');
            } else if (data.msg === "try_again") {
                swal_settings('error', 'عذراً، الرجاء المحاولة فيما بعد');
            } else if (data.msg === "isExist") {
                swal_settings('error', 'البريد الإلكتروني الجديد موجود مسبقاً');
            } else if (data.msg === "EmailContextError") {
                swal_settings('error', 'تأكد من إدخال البريد الإلكتروني بشكل صحيح');
            } else if (data.msg === "NoAnyChange") {
                swal_settings('error', 'لم تحدث أي تغيير على البيانات المخزنة لدينا');
            } else if (data.msg === "Done") {
                swal_settings('success', 'تمت العملية بنجاح');
                setTimeout(function () {
                    location.reload();
                }, 2500);
            } else if (data.msg === "Fail") {
                swal_settings('error', 'عذراً، فشلت العملية');
            } else if (data.msg === "inCorrectEmail") {
                swal_settings('error', 'البريد الإلكتروني الحالي غير مطابق لما هو مسجل لدينا');
            }
        }
    });
    return false;
});

$("#Change_Password_Submit").click(function (ev) {
    $("#parent_loader").css('display', 'block');
    ev.preventDefault();
    $.ajax({
        type: "POST",
        url: $("meta[property='change_password']").attr('content'),
        data: $('#Change_Password_Form').serialize(),
        success: function (data) {
            $("#parent_loader").css('display', 'none');
            if (data.msg === "NotActive") {
                location.reload();
            } else if (data.msg === "isEmpty") {
                swal_settings('error', 'الرجاء إدخال جميع البيانات');
            } else if (data.msg === "try_again") {
                swal_settings('error', 'عذراً، الرجاء المحاولة فيما بعد');
            } else if (data.msg === "isNotMatch") {
                swal_settings('error', 'كلمة المرور غير متطابقة في كلا الحقلين');
            } else if (data.msg === "PasswordContextError") {
                swal_settings('error', 'عذراً، تنسيق كلمة المرور مرفوض');
            } else if (data.msg === "NoAnyChange") {
                swal_settings('error', 'لم تحدث أي تغيير على البيانات المخزنة لدينا');
            } else if (data.msg === "Done") {
                swal_settings('success', 'تمت العملية بنجاح');
                setTimeout(function () {
                    location.reload();
                }, 2500);
            } else if (data.msg === "Fail") {
                swal_settings('error', 'عذراً، فشلت العملية');
            } else if (data.msg === "inCorrectPassword") {
                swal_settings('error', 'كلمة المرور الحالية غير مطابقة لما هو مسجل لدينا');
            }
        }
    });
    return false;
});
