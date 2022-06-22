document.addEventListener("DOMContentLoaded", init, false)

function init() {
    let body_element = document.querySelector("body");
    let new_element = document.createElement("p");
    body_element.appendChild(new_element);
    new_element.innerHTML = "Third paragraph";
}