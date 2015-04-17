/**
 * Created by Administrator on 2015/4/16.
 */
function sendblog(){
    $.ajax({
        url: '/timeline/sendblog/',
        type: 'POST',
        data: $('.talkBox').serialize(),
        success: function (r) {
            console.log(r);
            if (r == '200') {
                location.reload(true)
            }
        },
        error: function(r) {
            console.log(r)
        }
    });
}
