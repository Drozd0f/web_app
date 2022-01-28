let popup = document.getElementById("popup")

function showPopup() {
    if (popup.textContent !== 'user not exists') {
        popup.classList.toggle("show")
    }
}

showPopup()

window.onclick = function (e) {
    if (e.target !== popup) {
        popup.classList.remove("show")
    }
}
