$(function () {
  $('[type="submit"]').click(function () {
    $(this).prop("disabled", true); //ボタンを無効化する

    $("#cancel-btn").css("pointer-events", "none").attr("tabindex", -1); //aタグ(キャンセルボタン)を非活性化

    $("#loading").removeClass("d-none"); // スピナーを表示させる

    $(this).closest("form").submit(); //フォームを送信する
  });
});
