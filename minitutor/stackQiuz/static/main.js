$(document).ready(function () {
    getQuiz(1);
    tab_acv();
    $('.tab2-content').hide();
})

let idx = 1
let ans='';

function getQuiz(idx){
    console.log("%d 문제입니다.",idx)
    $.ajax({
        url: `/quiz?idx=${idx}`,
        method: 'GET',
        success: function (response){
            $('.quiz-content').empty();
            $('.quiz-content').append(response["quiz"])
        }
    })
}

function btn_click(x){
    console.log("%s 선택.",x)
    ans += x;

    idx +=1;

    if (idx > 4){
        alert("최종 응답 유형은 "+ ans)
        window.location.reload();
        return
    }
    getQuiz(idx,x)

}

function tab_acv(){
    $('#tab1').on('click', function () {
        $('#tab1').addClass('acv')
        $('#tab2').removeClass('acv')
        $('.tab1-content').show();
        $('.tab2-content').hide();
    })

    $('#tab2').on('click', function () {
        $('#tab1').removeClass('acv')
        $('#tab2').addClass('acv')
        $('.tab2-content').show();
        $('.tab1-content').hide();
    })
}

