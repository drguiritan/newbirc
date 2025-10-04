"use strict";

var theme = {
  init: function () {
    theme.menu();
  },

  menu: function () {
    document.querySelectorAll(".dropdown-menu a.dropdown-toggle").forEach(function (el) {
      el.addEventListener("click", function (e) {
        // Close any other open submenu
        if (!this.nextElementSibling.classList.contains("show")) {
          const openSubmenus = this.closest(".dropdown-menu").querySelectorAll(".show");
          openSubmenus.forEach(function (submenu) {
            submenu.classList.remove("show");
          });
        }

        // Toggle the clicked submenu
        this.nextElementSibling.classList.toggle("show");

        // Cleanup on dropdown hide
        const parentDropdown = this.closest("li.nav-item.dropdown.show");
        if (parentDropdown) {
          parentDropdown.addEventListener("hidden.bs.dropdown", function () {
            const opened = parentDropdown.querySelectorAll(".show");
            opened.forEach(function (submenu) {
              submenu.classList.remove("show");
            });
          });
        }

        e.preventDefault();
        e.stopPropagation();
      });
    });
  }
};

theme.init();

// ====================
// Offcanvas Navbar
// ====================
var navbar = document.querySelector(".navbar");
const navOffCanvasBtn = document.querySelectorAll(".offcanvas-nav-btn"),
      navOffCanvas = document.querySelector(".navbar:not(.navbar-clone) .offcanvas-nav");

let bsOffCanvas;

function toggleOffCanvas() {
  if (bsOffCanvas) {
    if (bsOffCanvas._isShown) {
      bsOffCanvas.hide();
    } else {
      bsOffCanvas.show();
    }
  }
}

if (navOffCanvas) {
  bsOffCanvas = new bootstrap.Offcanvas(navOffCanvas, { scroll: true });
  navOffCanvasBtn.forEach((btn) => {
    btn.addEventListener("click", () => {
      toggleOffCanvas();
    });
  });
}
