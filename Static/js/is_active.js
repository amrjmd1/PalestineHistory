$(document).ready(function () {
    sweet_alert();
});

function sweet_success() {
    title = "تمت عملية التحقق بنجاح";
    swal({
        position: 'center',
        type: 'success',
        html: '<p class="html_swal">' + title + '</p>',
        showConfirmButton: false,
        allowOutsideClick: false,
        timer: 3000
    }).catch(swal.noop);
    setTimeout(function () {
        location.reload();
    }, 3000);
}

function sweet_warning(message) {
    if (message === "") {
        type = "warning";
        title = "لن تستيطع الإستفادة من حسابك الشخصي قبل التحقق من صحة البريد الإلكتروني";
    } else {
        type = "error";
        title = "الرجاء التحقق من رمز التحقق";
    }
    swal({
        position: 'center',
        type: type,
        html: '<p class="html_swal">' + title + '</p>',
        showConfirmButton: true,
        allowOutsideClick: false,
        confirmButtonText: 'التحقق الآن'
    }).then(function (result) {
        if (result) {
            sweet_alert();
        }
    })
}

function sweet_alert() {
    swal({
        title: '<p id="title_swal">التحقق من البريد الإلكتروني</p>',
        html: '<p class="html_swal">قم بمراجعة البريد الإلكتروني الخاص بك ، ثم قم بإدراج رمز التحقق المكون من 6 أرقام</p>',
        input: 'text',
        inputAttributes: {
            'maxlength': 6,
            'id': 'input_verify_email'
        },
        confirmButtonText: 'التحقق الآن',
        allowOutsideClick: false
    }).then(function (result) {
        if (!result) {
            sweet_warning("");
        } else {
            if (isNaN(result)) {
                sweet_warning('isNaN');
            } else {
                $.ajax({
                    type: "POST",
                    url: $("meta[property='Check_Verify_Code']").attr('content'),
                    data: {
                        'code': result,
                        csrfmiddlewaretoken: $("meta[property='csrfmiddlewaretoken']").attr('content')
                    },
                    success: function (data) {
                        if (data.msg === 'empty') {
                            sweet_warning();
                        } else if (data.msg === 'Fail') {
                            sweet_warning('Fail');
                        } else if (data.msg === 'Done') {
                            sweet_success();
                        }
                    }
                });
            }
        }

    })
}
