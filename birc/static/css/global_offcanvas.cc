/* === Mobile Offcanvas Styling === */
.offcanvas {
  max-width: 300px;
}

.offcanvas-header {
  border-bottom: 2px solid rgba(255, 255, 255, 0.2);
}

.offcanvas-title {
  font-family: "Baloo 2", sans-serif;
  font-weight: bold;
  font-size: 1.5rem;
}

.offcanvas-body {
  background-color: var(--white);
}

/* Mobile nav items */
.offcanvas-body .navbar-nav {
  width: 100%;
}

.offcanvas-body .nav-item {
  border-bottom: 1px solid rgba(197, 197, 197, 0.3);
}

.offcanvas-body .nav-item:last-child {
  border-bottom: none;
}

/* Mobile nav links */
.offcanvas-body .nav-link {
  color: var(--dark) !important;
  font-weight: 500;
  transition: background-color 0.3s, color 0.3s, padding-left 0.3s;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.offcanvas-body .nav-link:hover {
  background-color: var(--green);
  color: var(--white) !important;
  padding-left: 1.5rem !important;
}

/* Section headers (Services, Research, About Us) */
.offcanvas-body .nav-link.fw-bold {
  color: var(--green) !important;
  font-family: "Baloo 2", sans-serif;
  cursor: pointer;
}

.offcanvas-body .nav-link.fw-bold:hover {
  background-color: var(--green);
  color: var(--white) !important;
}

/* Arrow rotation for collapsible sections */
.offcanvas-body .nav-link[aria-expanded="true"] img {
  transform: rotate(180deg);
  filter: brightness(0) saturate(100%) invert(100%);
}

.offcanvas-body .nav-link img {
  transition: transform 0.3s ease, filter 0.3s;
}

/* Collapsed submenu styling */
.offcanvas-body .collapse {
  background-color: var(--light-gray);
}

.offcanvas-body .collapse .list-unstyled {
  margin: 0;
  padding: 0.5rem 0;
}

.offcanvas-body .collapse .nav-link {
  color: var(--dark) !important;
  font-weight: 400;
  padding: 0.75rem 1rem 0.75rem 2rem !important;
  position: relative;
}

.offcanvas-body .collapse .nav-link::before {
  content: '•';
  position: absolute;
  left: 1.5rem;
  color: var(--green);
  font-weight: bold;
}

.offcanvas-body .collapse .nav-link:hover {
  background-color: var(--yellow);
  color: var(--dark) !important;
  padding-left: 2.5rem !important;
}

.offcanvas-body .collapse .nav-link:hover::before {
  color: var(--dark);
}

/* Home icon styling */
.offcanvas-body .bi-house {
  color: var(--green);
  font-size: 1.2rem;
  transition: color 0.3s;
}

.offcanvas-body .nav-link:hover .bi-house {
  color: var(--white);
}

/* Close button customization */
.btn-close-white {
  filter: brightness(0) invert(1);
  opacity: 0.8;
  transition: opacity 0.3s, transform 0.3s;
}

.btn-close-white:hover {
  opacity: 1;
  transform: rotate(90deg);
}

/* Smooth transitions for collapse */
.offcanvas-body .collapse {
  transition: height 0.35s ease;
}

/* Active state for current page */
.offcanvas-body .nav-link.active {
  background-color: var(--green);
  color: var(--white) !important;
  border-left: 4px solid var(--yellow);
}

/* Responsive adjustments */
@media (max-width: 576px) {
  .offcanvas {
    max-width: 280px;
  }
  
  .offcanvas-title {
    font-size: 1.3rem;
  }
  
  .offcanvas-body .nav-link {
    font-size: 0.95rem;
    padding: 0.85rem 1rem !important;
  }
}