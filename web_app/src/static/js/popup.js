let popup = document.getElementById("popup")

function showPopup() {
    popup.classList.toggle("show")
}

showPopup()

window.onclick = function (e) {
    if (e.target !== popup) {
        popup.classList.remove("show")
    }
}
