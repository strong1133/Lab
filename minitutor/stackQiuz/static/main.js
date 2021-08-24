$(document).ready(function () {
    getQuiz(1);
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
