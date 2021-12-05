sidebar = document.querySelector(".sidebar");

sidebar.onmouseover = function () {
    sidebar.style.right = "-20px";
}

sidebar.onmouseout = function () {
    sidebar.style.right = "-240px";
}

timeinput = document.getElementById("inputTime");
submitButton = document.getElementById("submitButton");

submitButton.onclick = async function () {
    let url = 'http://127.0.0.1:5000/?date=' + Date.parse(timeinput.value)
    let response = await fetch(url);
    return await response.json()
}