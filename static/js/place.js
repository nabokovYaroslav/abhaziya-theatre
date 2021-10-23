// Change Language

const langOne = document.querySelector(".langButtonOne");
const langTwo = document.querySelector(".langButtonTwo");
langOne.addEventListener("click", (e) => {
  e.preventDefault();
  langOne.classList.add("activeLang");
  langTwo.classList.remove("activeLanguage");
});

langTwo.addEventListener("click", (e) => {
  e.preventDefault();
  langTwo.classList.add("activeLanguage");
  langOne.classList.remove("activeLang");
});

// burgerButton

const burgerContainer = document.querySelector(".burger_menu");
const burgerButton = document.querySelector(".burgerButton");
const burgerButtonAlt = document.querySelector(".burgerButtonAnother");
burgerButton.addEventListener("click", (e) => {
  e.preventDefault();
  burgerContainer.classList.add("activeBurger");
});
burgerButtonAlt.addEventListener("click", (e) => {
  e.preventDefault();
  burgerContainer.classList.add("activeBurger");
});

// closeBurgerBtn

const closeBurger = document.querySelector(".burgerCloseBtn");

closeBurger.addEventListener("click", (e) => {
  e.preventDefault();
  burgerContainer.classList.remove("activeBurger");
});

let url = window.location;

window.onload = () => {
  function getCookie(name) {
    let matches = document.cookie.match(
      new RegExp(
        "(?:^|; )" +
          name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, "\\$1") +
          "=([^;]*)"
      )
    );
    return matches ? decodeURIComponent(matches[1]) : undefined;
  }

  const csrftoken = getCookie("csrftoken");

  function csrfSafeMethod(method) {
    return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
  }
  $.ajaxSetup({
    beforeSend: function (xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    },
  });
  $.ajax({
    url: `${url.href}get-map/`,
    method: "get",
    datatype: "html",
    data: {},
    success: function (map_url) {
      $.ajax({
        url: url.origin + map_url,
        method: "get",
        datatype: "xml",
        data: {},
        success: function (svg) {
          var dataSvg = $(svg).find("svg");
          $(".place_map").append(dataSvg.clone());
          $.ajax({
            url: `${url.href}get-tickets/`,
            method: "get",
            datatype: "json",
            data: {},
            success: function (tickets) {
              init_map(tickets);
            },
          });
        },
      });
    },
  });
};

function init_map(tickets) {
  tickets.forEach((ticket) => {
    seat = document.querySelector(
      `circle[data-seat-id='${ticket["fields"]["seat_id"]}']`
    );
    seat.classList.add("open");
    seat.setAttribute("data-ticket-id", ticket["pk"]);
    seat.setAttribute("data-event-id", ticket["fields"]["poster"]);
    seat.setAttribute("data-row-number", ticket["fields"]["row_number"]);
    seat.setAttribute("data-seat-number", ticket["fields"]["seat_number"]);
    seat.setAttribute("data-price", ticket["fields"]["price"]);
    seat.setAttribute("data-sector", ticket["fields"]["sector"]);
    seat.addEventListener("mouseenter", seatMouseEnter);
    seat.addEventListener("mouseleave", seatMouseLeave);
    seat.addEventListener("click", setSeatOnClick);
    seat.addEventListener("touchend", setSeatOnClick);
  });
  getCart();
  const svg = document.querySelector("svg");
  const panzoom = svgPanZoom(svg, {
    zoomScaleSensitivity: 0.5,
    onZoom: seatMouseLeave,
  });
  window.addEventListener("resize", () => {
    panzoom.resize();
    panzoom.fit();
    panzoom.center();
  });
  const control_minus = document.querySelector(".control_minus");
  const control_plus = document.querySelector(".control_plus");
  control_minus.addEventListener("click", () => {
    panzoom.zoomOut();
  });
  control_plus.addEventListener("click", () => {
    panzoom.zoomIn();
  });
  $(".loader")[0].classList.remove("active");
}

function seatMouseEnter(e) {
  const tooltip = document.querySelector(".tooltip");
  const arr = document.querySelector(".arr");
  const arrBox = arr.getBoundingClientRect();
  const circleBox = e.target.getBoundingClientRect();
  const svgBox = document.querySelector("svg").getBoundingClientRect();
  const svgTop = svgBox.y;
  const circleTop = circleBox.y;
  const circleTopofSvg = circleTop - svgTop;
  const svgLeft = svgBox.x;
  const svgRight = document.body.clientWidth - (svgLeft + svgBox.width);
  const circleLeft = circleBox.x;
  const circleRight =
    document.body.clientWidth - (circleLeft + circleBox.width);
  const circleLeftofSvg = circleLeft - svgLeft;
  const circleRightofSvg = circleRight - svgRight;
  let scrollWidth = document.body.offsetWidth - document.body.clientWidth;
  let tooltipTop = 0,
    tooltipLeft = 0,
    tooltipRight = 0,
    tooltipMarginLeft = 0,
    tooltipMarginRight = 0,
    arrTop = 0,
    arrLeft = 0,
    arrRight = 0;
  tooltip.querySelector(".sector").textContent =
    e.target.getAttribute("data-sector");
  tooltip.querySelector(".row").textContent =
    "ряд " + e.target.getAttribute("data-row-number");
  tooltip.querySelector(".seat").textContent =
    "место " + e.target.getAttribute("data-seat-number");
  tooltip.querySelector(".price").textContent =
    e.target.getAttribute("data-price") + "р";
  if (circleTop - (tooltip.clientHeight - arrBox.height / 2) >= 0) {
    tooltipTop = circleTopofSvg - tooltip.clientHeight - arrBox.height / 2;
    arrTop = circleTopofSvg - arrBox.height / 2;
  } else {
    tooltipTop = circleTopofSvg + circleBox.height + arrBox.height / 2;
    arrTop = circleTopofSvg + circleBox.height;
    arr.classList.add("top");
  }
  if (circleLeft - (tooltip.clientWidth - circleBox.width) / 2 < 0) {
    tooltipLeft = circleLeftofSvg - (tooltip.clientWidth - circleBox.width) / 2;
    tooltipMarginLeft = -(
      circleLeft -
      (tooltip.clientWidth - circleBox.width) / 2
    );
    arrLeft = circleLeftofSvg - (arrBox.width - circleBox.width) / 2;
  } else if (circleRight - (tooltip.clientWidth - circleBox.width) / 2 < 0) {
    tooltipRight =
      circleRightofSvg - (tooltip.clientWidth - circleBox.width) / 2;
    tooltipMarginRight = -(
      circleRight -
      (tooltip.clientWidth - circleBox.width) / 2
    );
    arrRight = circleRightofSvg - (arrBox.width - circleBox.width) / 2;
  } else {
    tooltipLeft = circleLeftofSvg - (tooltip.clientWidth - circleBox.width) / 2;
    if (circleRight < circleLeft) {
      arrRight = circleRightofSvg - (arrBox.width - circleBox.width) / 2;
    } else {
      arrLeft = circleLeftofSvg - (arrBox.width - circleBox.width) / 2;
    }
  }
  tooltip.style.top = tooltipTop + "px";
  tooltip.style.left = tooltipLeft != 0 ? tooltipLeft + "px" : "auto";
  tooltip.style.right =
    tooltipRight != 0 ? tooltipRight + scrollWidth + "px" : "auto";
  tooltip.style.marginLeft = tooltipMarginLeft + "px";
  tooltip.style.marginRight = tooltipMarginRight + "px";
  arr.style.top = arrTop + "px";
  arr.style.left = arrLeft != 0 ? (arrLeft < 0 ? 0 : arrLeft + "px") : "auto";
  arr.style.right =
    arrRight != 0 ? (arrRight < 0 ? 0 : arrRight + "px") : "auto";
  tooltip.classList.add("show");
  arr.classList.add("show");
}

function seatMouseLeave(e) {
  const tooltip = document.querySelector(".tooltip");
  const arr = document.querySelector(".arr");
  tooltip.classList.remove("show");
  tooltip.style.top = 0;
  tooltip.style.left = 0;
  tooltip.style.right = "auto";
  tooltip.style.marginLeft = 0;
  tooltip.style.marginRight = 0;
  arr.classList.remove("show");
  arr.style.top = 0;
  arr.style.left = 0;
  arr.style.right = "auto";
  arr.classList.remove("top");
}

function setSeatOnClick(e) {
  $(".loader")[0].classList.add("active");
  const seat = e.target;
  seat.removeEventListener("click", setSeatOnClick);
  seat.removeEventListener("touchend", setSeatOnClick);
  const ticket_id = seat.getAttribute("data-ticket-id");
  $.ajax({
    url: `${url.origin}/api/cart/add/`,
    method: "post",
    datatype: "json",
    data: {
      ticket_id: ticket_id,
    },
    success: function (message) {
      seat.classList.remove("open");
      seat.classList.add("your");
      seat.addEventListener("click", removeSeatOnClick);
      seat.addEventListener("touchend", removeSeatOnClick);
      new Toast({
        title: false,
        text: message.text,
        theme: "success",
        autohide: true,
        interval: 7000,
      });
      getCart();
      return false;
    },
    error: function (jqXHR, exception) {
      seat.classList.remove("open");
      seat.addEventListener("click", removeSeatOnClick);
      seat.addEventListener("touchend", removeSeatOnClick);
      if (jqXHR.status == 403) {
        new Toast({
          title: "Ошибка",
          text: jqXHR.responseJSON.error,
          theme: "danger",
          autohide: true,
          interval: 7000,
        });
      }
      getCart();
      return false;
    },
  });
}

function removeSeatOnClick(e) {
  $(".loader")[0].classList.add("active");
  const seat = e.target;
  seat.removeEventListener("click", removeSeatOnClick);
  seat.removeEventListener("touchend", removeSeatOnClick);
  const ticket_id = seat.getAttribute("data-ticket-id");
  $.ajax({
    url: `${url.origin}/api/cart/remove/`,
    method: "post",
    datatype: "json",
    data: {
      ticket_id: ticket_id,
    },
    success: function (message) {
      seat.classList.remove("your");
      seat.classList.add("open");
      seat.addEventListener("click", setSeatOnClick);
      seat.addEventListener("touchend", setSeatOnClick);
      new Toast({
        title: false,
        text: message.text,
        theme: "success",
        autohide: true,
        interval: 7000,
      });
      getCart();
      return false;
    },
    error: function (jqXHR, exception) {
      seat.classList.remove("your");
      seat.classList.add("open");
      seat.addEventListener("click", setSeatOnClick);
      seat.addEventListener("touchend", setSeatOnClick);
      if (jqXHR.status == 404) {
        new Toast({
          title: "Ошибка",
          text: jqXHR.responseJSON.error,
          theme: "danger",
          autohide: true,
          interval: 7000,
        });
      }
      getCart();
      return false;
    },
  });
}

function getCart() {
  $.ajax({
    url: `${url.origin}/api/cart/get/`,
    method: "get",
    datatype: "json",
    data: {},
    success: function (cart) {
      let index = 1;
      let cart_template = "";
      cart["tickets"].forEach((ticket) => {
        seat = document.querySelector(
          `circle[data-seat-id='${ticket["seat_id"]}']`
        );
        seat.classList.add("your");
        seat.setAttribute("data-ticket-id", ticket["ticket_id"]);
        seat.setAttribute("data-row-number", ticket["row_number"]);
        seat.setAttribute("data-seat-number", ticket["seat_number"]);
        seat.setAttribute("data-price", ticket["price"]);
        seat.setAttribute("data-sector", ticket["sector"]);
        seat.addEventListener("mouseenter", seatMouseEnter);
        seat.addEventListener("mouseleave", seatMouseLeave);
        seat.addEventListener("click", removeSeatOnClick);
        seat.addEventListener("touchend", removeSeatOnClick);
        cart_template +=
          '<div class="pay_left_body_inner"><h4 class="disApear">' +
          index +
          "</h4><p>" +
          ticket["title"] +
          "</p><h4>" +
          ticket["start_date"] +
          "</h4><h4>" +
          ticket["sector"] +
          "/ряд " +
          ticket["row_number"] +
          "/место " +
          ticket["seat_number"] +
          "</h4><h3>" +
          ticket["price"] +
          "р" +
          `</h3><i class="fas fa-times" data-ticket-id="${ticket["ticket_id"]}" aria-hidden="true"></i></div>`;
        index++;
      });
      cart_template +=
        '<div class="pay_left_body_result"><h3>итого</h3><h3>' +
        cart["total"] +
        "р</h3></div>";
      document.querySelector(".pay_left_body").innerHTML = cart_template;
      document.querySelectorAll("i.fas.fa-times").forEach((button) => {
        button.addEventListener("click", (e) => {
          $(".loader")[0].classList.add("active");
          const button = e.target;
          button.onclick = null;
          const ticket_id = button.getAttribute("data-ticket-id");
          const seat = document.querySelector(
            `circle[data-ticket-id='${ticket_id}']`
          );
          $.ajax({
            url: `${url.origin}/api/cart/remove/`,
            method: "post",
            datatype: "json",
            data: {
              ticket_id: ticket_id,
            },
            success: function (message) {
              seat.classList.remove("your");
              seat.classList.add("open");
              seat.removeEventListener("click", removeSeatOnClick);
              seat.removeEventListener("touchend", removeSeatOnClick);
              seat.addEventListener("click", setSeatOnClick);
              seat.addEventListener("touchend", setSeatOnClick);
              new Toast({
                title: false,
                text: message.text,
                theme: "success",
                autohide: true,
                interval: 7000,
              });
              getCart();
            },
            error: function (jqXHR, exception) {
              if (jqXHR.status == 404) {
                new Toast({
                  title: "Ошибка",
                  text: jqXHR.responseJSON.error,
                  theme: "danger",
                  autohide: true,
                  interval: 7000,
                });
              }
              getCart();
            },
          });
        });
      });
      $(".loader")[0].classList.remove("active");
    },
  });
}
