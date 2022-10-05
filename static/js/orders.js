(function () {
  // polyfill
  if (!Element.prototype.matches) 
    Element.prototype.matches = Element.prototype.msMatchesSelector;
  if (!Element.prototype.closest) {
    Element.prototype.closest = function (s) {
      var el = this;
      do {
        if (el.matches(s)) 
          return el;
        el = el.parentElement || el.parentNode;
      } while (el !== null && el.nodeType === 1);
      return null;
    };
  }

  let intervalId = null;

  // 値更新
  const valueUpdate = function (input, increment) {
    let value = parseFloat(input.value);
    const min = parseFloat(input.min);
    const max = parseFloat(input.max);
    const step = !isNaN(parseFloat(input.step))
      ? parseFloat(input.step)
      : 1;

    value = (
      isNaN(value)
      ? 0
      : value) + (
      increment
      ? step
      : -step);

    if (!isNaN(min) && value < min) 
      input.value = min;
    else if (!isNaN(max) && value > max) 
      input.value = max;
    else 
      input.value = value;
    }
  ;
  // クリック時
  const click = function (t) {
    if (t.matches(".spin .spin-minus, .spin .spin-plus")) {
      if (intervalId != null) 
        return;
      const input = t.closest(".spin").querySelector(".spin-input");
      if (!input) 
        return;
      
      valueUpdate(input, t.matches(".spin-plus"));
    }
  };
  // マウス・タッチ開始時
  const down = function (t) {
    if (t.matches(".spin .spin-minus, .spin .spin-plus")) {
      const input = t.closest(".spin").querySelector(".spin-input");
      if (!input) 
        return;
      const increment = t.matches(".spin-plus");

      let delay = 500;
      let start = new Date().getTime();
      intervalId = setInterval(function () {
        if (new Date().getTime() - start <= delay) 
          return; // 開始の間隔をずらす (clickとの兼ね合い)
        valueUpdate(input, increment);
      }, 50);
    }
  };
  // マウス・タッチ終了時
  const up = function (t) {
    if (t.matches(".spin .spin-minus, .spin .spin-plus")) {
      clearInterval(intervalId);
      intervalId = null;
    }
  };

  document.addEventListener("click", function (e) {
    click(e.target);
  });

  document.addEventListener("mousedown", function (e) {
    down(e.target);
  });
  document.addEventListener("mouseup", function (e) {
    up(e.target);
  });

  document.addEventListener("touchstart", function (e) {
    down(e.target);
  });
  document.addEventListener("touchend", function (e) {
    up(e.target);
  });
})();

// input[type=number] 入力調整
(function () {
  if (!Element.prototype.matches) 
    Element.prototype.matches = Element.prototype.msMatchesSelector;
  document.addEventListener("input", function (e) {
    if (e.target.matches("input[type=number]")) {
      const input = e.target;
      const value = parseFloat(input.value);
      const min = parseFloat(input.min);
      const max = parseFloat(input.max);

      if (!isNaN(min) && value < min) 
        input.value = min;
      else if (!isNaN(max) && value > max) 
        input.value = max;
      }
    });
})();