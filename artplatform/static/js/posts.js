

function wireAllEventListeners() {
  const newpostButton = document.getElementById("add-post")
  newpostButton.addEventListener("click", () => {
    newpostButton.style.display = "none"
    document.getElementById("new-post").style.display = "block"
  })
}

window.onload = () => {
  wireAllEventListeners()
}

