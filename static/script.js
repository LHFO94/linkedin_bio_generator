// get the button and the spinner elements
const button = document.getElementById("btn_submit");
const spinner = document.getElementById("spinner");
const copyIcon = document.getElementById('copy_button')

// adds a spinner to the loading button when clicked
button.addEventListener("click", function () {
    button.innerHTML = '<span class="spinner-grow spinner-grow-sm d-none" role="status" id="spinner" aria-hidden="true"></span>Loading...';
    document.getElementById('spinner').classList.remove('d-none');
});

// form validation functionality
document.addEventListener('input', function (event) {
    if (event.target.tagName.toLowerCase() === 'input') {
        var form = document.querySelector('form');
        if (form.checkValidity() === false) {
            button.disabled = true;
            event.preventDefault();
            event.stopPropagation();
        }
        else {
            button.disabled = false;
        }
        form.classList.add('was-validated');
    }
});

// initializes the particles.js background
window.onload = function () {
    Particles.init({
        selector: '.background',
        maxParticles: 250,
        connectParticles: true,
        color: '#FFFFFF',
    });
}

// adds copy text functionality to copy button
copyIcon.addEventListener('click', () => {
    copyText = document.getElementById('bio_box');
    text = copyText.innerText;
    navigator.clipboard.writeText(text);
    if (copyIcon.name == 'checkmark-outline') {
        copyIcon.name = 'copy-outline';
        copyIcon.classList.add('active')
    }
    else {
        copyIcon.name = 'checkmark-outline'
        copyIcon.classList.remove('active')
    }
})