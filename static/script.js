// Select the button and the spinner elements
const button = document.getElementById("btn_submit");
const spinner = document.getElementById("spinner");
const url = document.getElementById('basic_url');

// Add a click event listener to the button
button.addEventListener("click", function () {
    // button.innerText = 'Loading...'
    button.innerHTML = '<span class="spinner-grow spinner-grow-sm d-none" role="status" id="spinner" aria-hidden="true"></span>Loading...';
    document.getElementById('spinner').classList.remove('d-none');
    //button.disabled = true
});

window.onload = function () {
    Particles.init({
        selector: '.background',
        maxParticles: 250,
        connectParticles: true,
        color: '#FFFFFF',
    });
}

// adds copy text functionality to copy_button
copyIcon = document.querySelector('#copy_button');
copyIcon.addEventListener('click', () => {
    copyText = document.getElementById('bio_box');
    text = copyText.innerText;
    navigator.clipboard.writeText(text);
})



// function myFunction() {
//     // Get the text field
//     var copyText = document.getElementById("bio_box");

//     // Select the text field
//     copyText.select();
//     copyText.setSelectionRange(0, 99999); // For mobile devices

//     // Copy the text inside the text field
//     navigator.clipboard.writeText(copyText.value);

//     // Alert the copied text
//     alert("Copied the text: " + copyText.value);
// }
//     output_box = document.getElementById('output_box');
//     if (output_box) {
//         console.log('output box found');
//         output_box.classList.remove('show');
//         setTimeout(function () {
//             output_box.classList.add('show');
//         }, 10);
//     };
// };

// document.addEventListener("DOMContentLoaded", function (event) {
//     // Your code to run since DOM is loaded and ready
//     animate_box();
// });

// function animate_box() {
//     output_box = document.getElementById('output_box');
//     if (output_box) {
//         console.log('box found')
//         output_box.classList.add('animated', 'fadeInDown');
//         setTimeout(function () {
//             output_box.classList.remove('fadeInDown');
//         }, 10000)
//     }
//     else {
//         console.log('box not found')
//         //pass
//     }
// 
// }