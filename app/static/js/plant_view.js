
function mute_toggle() {
    let button = document.getElementById("mute-button")
    let current_state = button.dataset.muted;
    console.log(current_state)
    if (current_state === "none" || current_state === "True") {
        console.log("unmuted")
        button.dataset.muted = "False"
        button.children.item(0).className = "bi bi-volume-up"
    } else {
        console.log("muted")
        button.dataset.muted = "True"
        button.children.item(0).className = "bi bi-volume-mute"
    }
}


window.addEventListener("load", () => {
    document.getElementById("mute-button").addEventListener("click", mute_toggle)
    mute_toggle()
})