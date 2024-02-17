
window.addEventListener("load", () => {
    let type = document.getElementById("auth-form").dataset.type
    console.log(type)

    document.getElementById("auth-form").addEventListener("submit", (e) => {
        e.preventDefault();

        let name = null
        if (type === "signup") {
            name = document.getElementById("name").value // Get Name
        }

        let email = document.getElementById("email").value // Get Email
        let password = document.getElementById("password").value // Get Password

        hash(password).then(hex_passhash => { // Hash Password
            let data = {
                "name": name,
                "email": email,
                "passhash": hex_passhash
            }
            let xhr = new XMLHttpRequest();
            xhr.open('POST', ((type === "login") ? "/login" : "/signup"), false);
            xhr.setRequestHeader("Content-Type", "application/json")
            xhr.send(JSON.stringify(data));
            if (xhr.status === 200) {
                let res = JSON.parse(xhr.responseText)
                hash(`${email}${hex_passhash}`).then(token => {
                    document.cookie = `token=${token}; path=/`
                    document.cookie = `userID=${res.id}; path=/`
                })
                document.location = "/profile"
            } else if (xhr.status === 400) {
                let res = JSON.parse(xhr.responseText)
                alert(res.message)
            } else {
                alert(xhr.responseText)
            }
        })
    })
})

