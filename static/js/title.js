// Change Language

const langOne = document.querySelector('.langButtonOne')
const langTwo = document.querySelector('.langButtonTwo')
langOne.addEventListener('click' , e => {
    e.preventDefault()
    langOne.classList.add('activeLang')
    langTwo.classList.remove('activeLanguage')
})

langTwo.addEventListener('click' , e => {
    e.preventDefault()
    langTwo.classList.add('activeLanguage')
    langOne.classList.remove('activeLang')
})

// burgerButton

const burgerContainer = document.querySelector('.burger_menu')
const burgerButton = document.querySelector('.burgerButton')
const burgerButtonAlt = document.querySelector('.burgerButtonAnother')
burgerButton.addEventListener('click' , e => {
    e.preventDefault() 
    burgerContainer.classList.add('activeBurger')
})
burgerButtonAlt.addEventListener('click' , e => {
    e.preventDefault() 
    burgerContainer.classList.add('activeBurger')
})

// closeBurgerBtn

const closeBurger = document.querySelector('.burgerCloseBtn')

closeBurger.addEventListener('click' , e => {
    e.preventDefault()
    burgerContainer.classList.remove('activeBurger')
})