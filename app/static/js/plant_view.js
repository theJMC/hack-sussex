
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
    play_sound()
}

function play_sound() {
    let button = document.getElementById("mute-button")
    let current_state = button.dataset.muted;
    let water_state = document.getElementById("water_val").value
    let sunlight_state = document.getElementById("sunlight_val").value
    console.log(parseInt(water_state))
    console.log(parseInt(sunlight_state))

    // if (current_state === "False") {
    if (parseInt(water_state)  > 80) {
        console.log("water")
        let under_the_water = document.getElementById("drowning")
        under_the_water.play()
    }
    if (parseInt(sunlight_state) < 20) {
        console.log("light")
        document.getElementById("scream").play()
    }
    if (parseInt(sunlight_state) >= 20 && parseInt(water_state) < 80) {
        console.log("all good")
        document.getElementById("just_right").play()

    }
    // }
}


window.addEventListener("load", () => {
    document.getElementById("mute-button").addEventListener("click", mute_toggle)
    mute_toggle()
})