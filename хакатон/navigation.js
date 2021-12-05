let button1 = document.querySelector(".button1");
let button2 = document.querySelector(".button2");
let button3 = document.querySelector(".button3");
let section1 = document.querySelector(".bio");
let section2 = document.querySelector(".googlemap");
let section3 = document.querySelector(".corespMatrix");
let hidden = document.querySelector(".hidden")

button1.onclick = function () {
    section2.classList.add("hidden");
    section3.classList.add("hidden");
    section1.classList.remove("hidden");
}

button2.onclick = function () {
    section1.classList.add("hidden");
    section3.classList.add("hidden");
    section2.classList.remove("hidden");
}

button3.onclick = function () {
    section1.classList.add("hidden");
    section2.classList.add("hidden");
    section3.classList.remove("hidden");
}

//set height for window
let h = document.documentElement.clientHeight;
section2.style.height = h - 55 + "px";
section1.style.height = h - 55 + "px";
section3.style.height = h - 55 + "px";
