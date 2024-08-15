//btnToTop
let mybutton = document.getElementById("btnToTop");
window.onscroll = function() {scrollFunction()};
function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        mybutton.style.display = "inline-flex";
    } else {
        mybutton.style.display = "none";
    }
}
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}
if (localStorage.getItem('theme') === 'dark') {
    document.body.classList.add('dark-mode');
}
document.getElementById('theme-toggle-button').addEventListener('click', function () {
    document.body.classList.toggle('dark-mode');
    if (document.body.classList.contains('dark-mode')) {
        localStorage.setItem('theme', 'dark');
    } else {
        localStorage.setItem('theme', 'light');
    }
});
// header fixed
function changeHeaderPosition() {
    const header = document.querySelector('.headerClass');
    const triggerHeight = window.innerHeight / 2;

    if (window.scrollY > triggerHeight) {
        header.classList.add('fixed');
    } else {
        header.classList.remove('fixed');
    }
}

// Add event listener for scroll event
window.addEventListener('scroll', changeHeaderPosition);
// page loading
window.addEventListener('load', function() {
    const loading = document.getElementById('loading');
    loading.style.opacity = '0'; // Start the fade-out animation
    setTimeout(() => {
        loading.style.display = 'none'; // Hide the loading screen after the transition
    }, 1000); // Wait for the transition duration
});