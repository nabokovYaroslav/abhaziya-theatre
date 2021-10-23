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
  let states = [];
  let index = 0;
  const audiosContainer = document.querySelectorAll(".radio_content");
  audiosContainer.forEach((container) => {
    /** Implementation of the presentation of the audio player */

    const playIconContainer = container.querySelector(".start");
    const seekSlider = container.querySelector(".seek-slider");
    let i = index;
    states[i] = "play";

    playIconContainer.addEventListener("click", () => {
      if (states[i] === "play") {
        audio.play();
        playIconContainer.querySelector(".play").style.display = "none";
        playIconContainer.querySelector(".pause").style.display = "block";
        requestAnimationFrame(whilePlaying);
        states[i] = "pause";
      } else {
        audio.pause();
        playIconContainer.querySelector(".pause").style.display = "none";
        playIconContainer.querySelector(".play").style.display = "block";
        cancelAnimationFrame(raf);
        states[i] = "play";
      }
    });

    const showRangeProgress = (rangeInput) => {
      if (rangeInput === seekSlider)
        container.style.setProperty(
          "--seek-before-width",
          (rangeInput.value / rangeInput.max) * 100 + "%"
        );
    };

    seekSlider.addEventListener("input", (e) => {
      showRangeProgress(e.target);
    });

    const audio = container.querySelector("audio");
    const durationContainer = container.querySelector(".duration");
    const currentTimeContainer = container.querySelector(".current-time");
    let raf = null;

    const calculateTime = (secs) => {
      const minutes = Math.floor(secs / 60);
      const seconds = Math.floor(secs % 60);
      const returnedSeconds = seconds < 10 ? `0${seconds}` : `${seconds}`;
      return `${minutes}:${returnedSeconds}`;
    };

    const displayDuration = () => {
      durationContainer.textContent = calculateTime(audio.duration);
    };

    const setSliderMax = () => {
      seekSlider.max = Math.floor(audio.duration);
    };

    const displayBufferedAmount = () => {
      const bufferedAmount = Math.floor(
        audio.buffered.end(audio.buffered.length - 1)
      );
      container.style.setProperty(
        "--buffered-width",
        `${(bufferedAmount / seekSlider.max) * 100}%`
      );
    };

    const whilePlaying = () => {
      seekSlider.value = Math.floor(audio.currentTime);
      currentTimeContainer.textContent = calculateTime(seekSlider.value);
      container.style.setProperty(
        "--seek-before-width",
        `${(seekSlider.value / seekSlider.max) * 100}%`
      );
      raf = requestAnimationFrame(whilePlaying);
    };

    if (audio.readyState > 0) {
      displayDuration();
      setSliderMax();
      displayBufferedAmount();
    } else {
      audio.addEventListener("loadedmetadata", () => {
        displayDuration();
        setSliderMax();
        displayBufferedAmount();
      });
    }

    audio.addEventListener("progress", displayBufferedAmount);

    seekSlider.addEventListener("input", () => {
      currentTimeContainer.textContent = calculateTime(seekSlider.value);
      if (!audio.paused) {
        cancelAnimationFrame(raf);
      }
    });

    seekSlider.addEventListener("change", () => {
      audio.currentTime = seekSlider.value;
      if (!audio.paused) {
        requestAnimationFrame(whilePlaying);
      }
    });
    index++;
  });
};
