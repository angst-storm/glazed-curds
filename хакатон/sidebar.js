sidebar = document.querySelector(".sidebar");

sidebar.onmouseover = function () {
    sidebar.style.right = "-20px";
}

sidebar.onmouseout = function () {
    sidebar.style.right = "-240px";
}

timeinput = document.getElementById("inputTime");
submitButton = document.getElementById("submitButton");

submitButton.onclick = function () {
    alert(timeinput.value);
}