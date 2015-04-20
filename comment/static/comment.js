/**
 * Created by Administrator on 2015/4/17.
 */

$(".int_like").click(function () {
    $(this).parent().parent().next().toggle();
})

function discuss(obj){
    $.ajax({
        url: '/comment/sendcomment/',
        type: 'POST',
        data: $(obj).parent().serialize(),
        success: function (r) {
            console.log(r);
            if (r == '200') {
                location.reload(true)
            }
        },
        error: function(r) {
            console.log(r)
        }
    })
}