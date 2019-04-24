var widthProgress = 0;
$(function () {
    $('[data-toggle="tooltip"]').tooltip({html: true});
    $('#register-carousel').carousel({interval: false});
    $('.next-interface').click(function () {
        var id_div = $(this).context.id;
        var inputs = $(this).parentsUntil('.my-carousel').children('form').children(),
            checkInput = true;
        inputs.each(function () {
            var input = $(this).children('input');
            if (input.hasClass('form-control')) {
                if (input.val().trim() == '') {
                    checkInput = false;
                    input.addClass('falseInput');
                    input.val('')
                } else {
                    input.removeClass('falseInput')
                }
            }
        });
        if (checkInput) {
            // verify email & password
            if (id_div === "next_register") {
                var id_msg_ver = "#show_message_Verify_Password";
                $.ajax({
                    type: "POST",
                    url: $("meta[property='verify_password']").attr('content'),
                    data: $('#Verify_Password_is_Valid').serialize(),
                    success: function (data) {
                        if (data.msg !== "isEmpty") {
                            if (data.msg === "isContextError")
                                showMeesage("عذراً! لقد قمت بتسجيل الدخول من حساب آخر", id_msg_ver);
                            else {
                                if (data.msg === "isExist")
                                    showMeesage("هذا الحساب بالفعل موجود مسبقاً", id_msg_ver);
                                else if (data.msg === "isNotMatch")
                                    showMeesage("تأكد من تطابق كلمة المرور في كلا الحقلين", id_msg_ver);
                                else if (data.msg === "isDone") {
                                    $(id_msg_ver).removeClass("alert alert-danger").html("");
                                    $('input[name="valid_email"]').val(data.valid_email);
                                    $('input[name="valid_password"]').val(data.valid_password);
                                    next_tab();
                                } else if (data.msg === "PasswordContextError")
                                    showMeesage("كلمة المرور غير مطابقة للشروط", id_msg_ver);
                            }
                        } else
                            showMeesage("تأكد من أكمال جميع الحقول", id_msg_ver);
                    }
                });
            } else if (id_div === "first_next") {
                next_tab();
            } else if (id_div === "create_account") { // create new account
                var id_msg_create = "#show_message_Data_Collection_Form";
                swal({
                    title: "هل أنت متأكد من بياناتك!",
                    text: "هذه البيانات سيتم إدراجها في سجلاتنا لنتحقق من مصداقية الأعضاء المشاركين في المسابقة",
                    icon: "warning",
                    button: {
                        text: "تسجيل البيانات",
                        closeModal: false
                    }
                }).then(function (isOk) {
                    if (isOk) {
                        $.ajax({
                            type: "POST",
                            url: $("meta[property='create_account']").attr('content'),
                            data: $('#Data_Collection_Form').serialize(),
                            success: function (data) {
                                if (data.msg === "isDone") {
                                    $(id_msg_create).removeClass("alert alert-danger").html("");
                                    $(".footer-register").remove();
                                    swal({
                                        title: "تم تسجيل بياناتك بنجاح",
                                        text: "ابدأ بتصفح موقعنا , نتمنى لك تجربة ممتعة ♥",
                                        icon: "success",
                                        button: "زيارة الحساب الشخصي"
                                    }).then(function () {
                                        window.location = data.url
                                    });
                                } else {
                                    swal.stopLoading();
                                    swal.close();
                                    if (data.msg !== "isEmpty") {
                                        if (data.msg === "GenderContextError")
                                            showMeesage("تأكد من حقل تحديد الجنس", id_msg_create);
                                        else if (data.msg === "isExist")
                                            showMeesage("هذا الحساب بالفعل موجود مسبقاً", id_msg_create);
                                        else if (data.msg === "EmailContextError")
                                            showMeesage("ربما عليك الرجوع خطوة للوراء للتأكد من البريد الإلكتروني", id_msg_create);
                                        else if (data.msg === "PasswordContextError")
                                            showMeesage("ربما عليك الرجوع خطوة للوراء للتأكد من كلمة المرور", id_msg_create);
                                        else if (data.msg === "PhoneContextError")
                                            showMeesage("تأكد من إدخال الهاتف المحمول بالصيغة الصحيحة", id_msg_create);
                                        else if (data.msg === "CategoryContextError")
                                            showMeesage("تأكد من تحديد الفئة بشكل صحيح", id_msg_create);
                                        else if (data.msg === "IdentityContextError")
                                            showMeesage("تأكد من إدخال هويتك بشكل صحيح", id_msg_create);
                                        else if (data.msg === "isFail")
                                            showMeesage("عذراً! فشل تسجيل بياناتك", id_msg_create);
                                        else if (data.msg === "try_again")
                                            showMeesage("عذراً! نواجه مشكلة في تسجيل بياناتك يرجى إعادة المحاولة", id_msg_create);
                                        else if (data.msg === "NameContextError")
                                            showMeesage("لا يمكن أن يحتوي الاسم على أرقام أو رموز", id_msg_create);
                                        else if (data.msg === "FailLogin")
                                            showMeesage("عذراً! لقد قمت بتسجيل الدخول من حساب آخر", id_msg_create);
                                    } else
                                        showMeesage("تأكد من إكمال جميع الحقول", id_msg_create);
                                }
                            }
                        });
                    }
                });
            }
        }
    });
    $('.show-password-click').click(function () {
        var $this = $(this);
        $this.hasClass('active') ? $this.removeClass('active') : $this.addClass('active');
        $this.prev().attr('type', function () {
            return $this.prev().attr('type') == 'password' ? 'text' : 'password';
        });
    });
    $('#password-register').focus(function () {
        $('#password-register-collapse').collapse('show')
    }).blur(function () {
        $('#password-register-collapse').collapse('hide')
    });
    $('.prev-interface').click(function () {
        $('#register-carousel').carousel('prev');
        var active = $('.my-progress .active-check').last(),
            data = $(this).data('prev');
        widthProgress -= 100 / ($('.circle').size() - 1);
        active.next().removeClass('active-now');
        $('.my-progress .fill').animate({
            width: '*%'.replace('*', widthProgress)
        }, 800, function () {
            active.removeClass('active-check').addClass('active-now').html(data);
        });

    });

    var reg_email = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/,
        en = /(?=(?:[^a-zA-Z\u0600-\u06FF]*[a-zA-Z\u0600-\u06FF]){2})/,
        number = /[ !@#$%^&*()_+\-=\[\]{}:\\|,.\/?0-9]/;

    function email_val() {
        if (reg_email.test($('#email-register').val())) {
            $('#password-register').removeAttr('disabled');
        } else {
            $('#password-register, #re_password, #next_register').attr('disabled', 'disabled').val('');
        }
    }

    $('#re_password').attr('disabled', 'disabled');
    email_val();
    $('#email-register').on('input propertychange', function () {
        email_val()
    });
    $('#password-register').on('input propertychange', function () {
        var val = $(this).val();
        if (val == "") {
            $("#email, #eight, #en, #code").removeClass("check-password")
            return
        }
        var email = function () {
                if (val.search($('#email-register').val().split('@')[0]) == -1) {
                    $('#email').addClass('check-password');
                    return true;
                } else {
                    $('#email').removeClass('check-password');
                    return false;
                }
            }(),
            length = function () {
                if (val.length >= 8) {
                    $('#eight').addClass('check-password');
                    return true;
                } else {
                    $('#eight').removeClass('check-password');
                    return false;
                }
            }(),
            english = function () {
                if (en.test(val)) {
                    $('#en').addClass('check-password');
                    return true;
                } else {
                    $('#en').removeClass('check-password');
                    return false;
                }
            }(),
            numbers = function () {
                if (number.test(val)) {
                    $('#code').addClass('check-password');
                    return true;
                } else {
                    $('#code').removeClass('check-password');
                    return false;
                }
            }();
        $('#re_password').attr('disabled', 'disabled').val('');
        email && length && english && numbers ? $('#re_password').removeAttr('disabled') : $('#re_password, #next_register').attr('disabled', 'disabled').val('');
    });
    $('#re_password').on('input propertychange', function () {
        if ($(this).val() == $('#password-register').val()) {
            $('#next_register').removeAttr('disabled');
        } else {
            $('#next_register').attr('disabled', 'disabled');
        }
    });
});

function showMeesage(text, id) {
    $(id).addClass("alert alert-danger").html(text)
}

function next_tab() {
    $('#register-carousel').carousel('next');
    var active = $('.my-progress .active-now');
    active.removeClass('active-now').addClass('active-check').html('<i class="fa fa-check"></i>');
    widthProgress += 100 / ($('.circle').size() - 1);
    $('.my-progress .fill').animate({
        width: '*%'.replace('*', widthProgress)
    }, 800, function () {
        active.next().addClass('active-now')
    });
}