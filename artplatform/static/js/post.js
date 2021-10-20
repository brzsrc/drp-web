
function wireAllEventListeners() {
    const cancelEditButton = document.getElementById("cancel-edit")
    const editpostButton = document.getElementById("edit-post")
    editpostButton.addEventListener("click", () => {
        document.getElementById("current-post").style.display = "none"
        document.getElementById("edit-panel").style.display = "block"
    })
    cancelEditButton.addEventListener("click", () => {
        document.getElementById("edit-panel").style.display = "none"
        document.getElementById("current-post").style.display = "block"
    })

}

window.onload = () => {
    wireAllEventListeners()
}

