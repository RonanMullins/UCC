let weight;
let weight_errors;
let height;
let height_errors;
let bmi;
let form;

document.addEventListener("DOMContentLoaded", init, false);

function init() {
    weight = document.querySelector("#weight")
    weight_errors = document.querySelector("#weight_errors");
    height = document.querySelector("#height");
    height_errors = document.querySelector("#height_errors");
    bmi = document.querySelector("#bmi");
    form = document.querySelector("form");
    form.addEventListener("submit", calculate_bmi, false);
}

function check_for_float(text, minimum, maximum) {
    let trimmed_text = text.trim();
    if (trimmed_text === "") {
        return "Required";
    }
    let number = parseFloat(trimmed_text);
    if (isNaN(number)) {
        return "Must be a number";
    }
    if (number < minimum) {
        return "Must be no less than " + minimum;
    }
    if (number > maximum) {
        return "Must be no greater than " + maximum;
    }
    return "";
}

function calculate_bmi(event) {
    let weight_error_message = check_for_float(weight.value, 10, 100)
    let height_error_message = check_for_float(height.value, 0.5, 2.5)
    if (weight_error_message || height_error_message) {
        weight_errors.innerHTML = weight_error_message;
        height_errors.innerHTML = height_error_message;
    } else {
        bmi.value = weight.value / (height.value * height.value)
    }
    event.preventDefault(); // dont send data to server, run client side
}