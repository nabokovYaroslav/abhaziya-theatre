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

window.onload = () => {
  $(".owl-carousel.first").owlCarousel({
    stagePadding: 50,
    margin: 20,
    autoplay: true,
    autoplayTimeout: 4000,
    autoplaySpeed: 1000,
    navSpeed: 500,
    autoplayHoverPause: true,
    loop: true,
    responsive: {
      0: {
        items: 1,
      },
      576: {
        items: 2,
      },
      768: {
        items: 3,
      },
    },
  });
  createNavForSlider(".owl-carousel.first");

  $(".image-carousel .owl-carousel").owlCarousel({
    stagePadding: 50,
    margin: 20,
    navSpeed: 500,
    loop: true,
    dots: false,
    responsive: {
      0: {
        items: 1,
      },
      576: {
        items: 2,
      },
      976: {
        items: 3,
      },
    },
  });
  createNavForSlider(".image-carousel .owl-carousel");

  function initImageCarousel() {
    let height = document.querySelector(".image-carousel").clientHeight - 100;
    document
      .querySelectorAll(".image-carousel .owl-item>div")
      .forEach((image) => {
        image.style.height = height + "px";
      });
  }
  initImageCarousel();
  window.addEventListener("resize", initImageCarousel);
  document
    .querySelector(".image-carousel .overlay")
    .addEventListener("click", () => {
      document.querySelector(".image-carousel").classList.remove("active");
    });
  document
    .querySelector(".image-carousel .overlay svg")
    .addEventListener("click", () => {
      document.querySelector(".image-carousel").classList.remove("active");
    });
  document.querySelectorAll(".info_child_left>div").forEach((image) => {
    image.addEventListener("click", () => {
      document.querySelector(".image-carousel").classList.add("active");
    });
  });
};

function createNavForSlider(selector) {
  var prevButton = document.createElement("button");
  prevButton.classList.add("prev");
  prevButton.addEventListener("click", () => {
    $(selector).trigger("prev.owl.carousel");
  });
  var nextButton = document.createElement("button");
  nextButton.classList.add("next");
  nextButton.addEventListener("click", () => {
    $(selector).trigger("next.owl.carousel");
  });
  prevButton.innerHTML =
    '<svg version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 256 256" style="enable-background:new 0 0 256 256;" xml:space="preserve"><g><g><polygon points="207.093,30.187 176.907,0 48.907,128 176.907,256 207.093,225.813 109.28,128"/></g></g></svg>';
  nextButton.innerHTML =
    '<svg version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"viewBox="0 0 256 256" style="enable-background:new 0 0 256 256;" xml:space="preserve"><g><g><polygon points="79.093,0 48.907,30.187 146.72,128 48.907,225.813 79.093,256 207.093,128"/></g></g></svg>';
  document.querySelector(selector).appendChild(prevButton);
  document.querySelector(selector).appendChild(nextButton);
}
