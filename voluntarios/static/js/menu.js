// voluntarios/static/js/menu.js
if (document.images) {
  designbuttonup = new Image();
  designbuttonup.src = "/static/img/up_01.gif";
  designbuttondown = new Image();
  designbuttondown.src = "/static/img/upo_01.gif";

  kodbuttonup = new Image();
  kodbuttonup.src = "/static/img/up_02.gif";
  kodbuttondown = new Image();
  kodbuttondown.src = "/static/img/upo_02.gif";

  supportbuttonup = new Image();
  supportbuttonup.src = "/static/img/up_03.gif";
  supportbuttondown = new Image();
  supportbuttondown.src = "/static/img/upo_03.gif";
}

function buttondown(buttonname) {
  if (document.images) {
      document[buttonname].src = eval(buttonname + "down.src");
  }
}

function buttonup(buttonname) {
  if (document.images) {
      document[buttonname].src = eval(buttonname + "up.src");
  }
}
