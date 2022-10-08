//同日2回目以降ローディング画面非表示
var loading_data = $.cookie("accessdate");
var myD = new Date();
var myYear = String(myD.getFullYear());
var myMonth = String(myD.getMonth() + 1);
var myDate = String(myD.getDate());

//開発時のみ下記の比較演算子は==で本番は!=に変更してください
if (loading_data != myYear + myMonth + myDate) {
  $("#loading").css("display", "block");
  setTimeout(function () {
    $("#loading_logo").fadeIn(1000, function () {
      setTimeout(function () {
        $("#loading_logo").fadeOut(1000);
      }, 1000);
      setTimeout(function () {
        $("#loading").fadeOut(1000, function () {
          var myD = new Date();
          var myYear = String(myD.getFullYear());
          var myMonth = String(myD.getMonth() + 1);
          var myDate = String(myD.getDate());
          $.cookie("accessdate", myYear + myMonth + myDate);
        });
      }, 1700);
    });
  }, 1000);
} else {
  $("#loading").css("display", "none"); //同日2回目のアクセスでローディング画面非表示
}
