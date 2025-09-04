let sidebar = document.querySelector(".sidebar");
let closeBtn = document.querySelector("#btn");
let searchBtn = document.querySelector(".bx-search");
document.addEventListener("DOMContentLoaded", () => {
  const updateWidth = () => {
    // set CSS variable ke :root
    document.documentElement.style.setProperty("--width", window.innerWidth);
    
    // kalau masih mau tampilkan angka juga
    const widthDisplayElement = document.getElementById("width-display");
    if (widthDisplayElement) {
      widthDisplayElement.textContent = window.innerWidth;
    }
  };

  updateWidth();
  window.addEventListener("resize", updateWidth);
});

closeBtn.addEventListener("click", () => {
    sidebar.classList.toggle("open");
    mainContent.classList.toggle("shifted");
    menuBtnChange();
})

searchBtn.addEventListener("click", () => {
    sidebar.classList.toggle("open");
    mainContent.classList.toggle("shifted");
    menuBtnChange();
})

function menuBtnChange() {
    if (sidebar.classList.contains("open")) {
        closeBtn.classList.replace("bx-menu", "bx-menu-alt-right");
    } else {
        closeBtn.classList.replace("bx-menu-alt-right", "bx-menu");
    }
}

var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}
menuBtnChange();
