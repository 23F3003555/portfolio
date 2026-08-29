const darkModeBtn = document.getElementById("darkModeBtn");

darkModeBtn.addEventListener("click", function () {

    document.body.classList.toggle("dark-mode");

    if (document.body.classList.contains("dark-mode")) {
        darkModeBtn.innerHTML = '<i class="fa-solid fa-sun"></i>';
    } else {
        darkModeBtn.innerHTML = '<i class="fa-solid fa-moon"></i>';
    }

});