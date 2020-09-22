$(function () {
    console.log('読み込み完了')

});


function execute() {
    console.log('実行ボタンクリック')

    var ua = navigator.userAgent.toLowerCase();
    if (ua.indexOf('chrome') == -1) {
        alert('GoogleChrome専用');
    }

    //入力値取得
    const login_url = $('#login_url').val()
    const buy_url = $('#buy_url').val()
    const mail = $('#mail').val()
    const password = $('#password').val()
    const launched_time = $('#launched_time').val()
    const ticket_type = $('#ticket_type').val()
    const ticket_num = $('#ticket_num').val()
    const cvs_type = $('#cvs_type').val()

    console.log('login_url' + ':' + login_url)
    console.log('buy_url' + ':' + buy_url)
    console.log('mail' + ':' + mail)
    console.log('password' + ':' + password)
    console.log('launched_time' + ':' + launched_time)
    console.log('ticket_type' + ':' + ticket_type)
    console.log('ticket_num' + ':' + ticket_num)
    console.log('cvs_type' + ':' + cvs_type)


    originalData = {
        login_url: login_url,
        buy_url: buy_url,
        mail: mail,
        password: password,
        launched_time: launched_time,
        ticket_type: ticket_type,
        ticket_num: ticket_num,
        cvs_type: cvs_type

    };

    const fileName = 'conf.json';
    const data = JSON.stringify(originalData);
    const link = document.createElement("a");
    link.href = "data:text/plain," + encodeURIComponent(data);
    link.download = fileName;
    link.click();
}