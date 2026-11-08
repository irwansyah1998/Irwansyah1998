"use strict";

(() => {
  const root = document.documentElement;
  const themeToggle = document.querySelector(".theme-toggle");
  const themeLabel = document.querySelector(".theme-label");
  const menuToggle = document.querySelector(".menu-toggle");
  const navigation = document.querySelector(".navigation");
  const navLinks = [...document.querySelectorAll(".nav-link")];
  const projectCards = [...document.querySelectorAll(".project-card")];
  const filterButtons = [...document.querySelectorAll(".filter-button")];
  const countOutput = document.querySelector("#visible-project-count");
  const backToTop = document.querySelector(".back-to-top-floating");
  const yearOutput = document.querySelector("#year");

  const setTheme = (theme, persist = true) => {
    root.dataset.theme = theme;
    const nextTheme = theme === "dark" ? "light" : "dark";
    const label = `Switch to ${nextTheme} theme`;
    themeToggle.setAttribute("aria-label", label);
    themeToggle.setAttribute("title", label);
    themeLabel.textContent = label;
    document.querySelector('meta[name="theme-color"]').content = theme === "dark" ? "#111214" : "#f5f5f0";
    if (persist) {
      try {
        localStorage.setItem("portfolio-theme", theme);
      } catch {
        // The current theme still works when storage is unavailable.
      }
    }
  };

  let initialTheme = "dark";
  try {
    const savedTheme = localStorage.getItem("portfolio-theme");
    if (savedTheme === "light" || savedTheme === "dark") initialTheme = savedTheme;
    else if (window.matchMedia("(prefers-color-scheme: light)").matches) initialTheme = "light";
  } catch {
    if (window.matchMedia("(prefers-color-scheme: light)").matches) initialTheme = "light";
  }
  setTheme(initialTheme, false);

  themeToggle.addEventListener("click", () => {
    setTheme(root.dataset.theme === "dark" ? "light" : "dark");
  });

  const closeMenu = (restoreFocus = false) => {
    navigation.classList.remove("is-open");
    menuToggle.setAttribute("aria-expanded", "false");
    menuToggle.querySelector(".sr-only").textContent = "Open navigation menu";
    if (restoreFocus) menuToggle.focus();
  };

  menuToggle.addEventListener("click", () => {
    const isOpen = menuToggle.getAttribute("aria-expanded") === "true";
    menuToggle.setAttribute("aria-expanded", String(!isOpen));
    menuToggle.querySelector(".sr-only").textContent = isOpen ? "Open navigation menu" : "Close navigation menu";
    navigation.classList.toggle("is-open", !isOpen);
    if (!isOpen) navigation.querySelector("a").focus();
  });

  navLinks.forEach((link) => link.addEventListener("click", () => closeMenu()));
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && menuToggle.getAttribute("aria-expanded") === "true") closeMenu(true);
  });
  document.addEventListener("click", (event) => {
    if (menuToggle.getAttribute("aria-expanded") === "true" &&
        !navigation.contains(event.target) &&
        !menuToggle.contains(event.target)) closeMenu();
  });

  const projectCounts = { all: projectCards.length };
  projectCards.forEach((card) => {
    projectCounts[card.dataset.status] = (projectCounts[card.dataset.status] || 0) + 1;
  });
  document.querySelectorAll("[data-count]").forEach((count) => {
    count.textContent = projectCounts[count.dataset.count] ?? 0;
  });

  filterButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const filter = button.dataset.filter;
      let visibleCount = 0;
      projectCards.forEach((card) => {
        const isVisible = filter === "all" || card.dataset.status === filter;
        card.hidden = !isVisible;
        if (isVisible) visibleCount += 1;
      });
      filterButtons.forEach((item) => {
        const isActive = item === button;
        item.classList.toggle("is-active", isActive);
        item.setAttribute("aria-pressed", String(isActive));
      });
      countOutput.textContent = visibleCount;
    });
  });

  if ("IntersectionObserver" in window) {
    const observedSections = [...document.querySelectorAll("main section[id]")];
    const sectionObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        navLinks.forEach((link) => {
          if (link.hash === `#${entry.target.id}`) link.setAttribute("aria-current", "location");
          else link.removeAttribute("aria-current");
        });
      });
    }, { rootMargin: "-25% 0px -65% 0px" });
    observedSections.forEach((section) => sectionObserver.observe(section));
  }

  let scrollScheduled = false;
  window.addEventListener("scroll", () => {
    if (scrollScheduled) return;
    scrollScheduled = true;
    window.requestAnimationFrame(() => {
      backToTop.classList.toggle("is-visible", window.scrollY > 560);
      scrollScheduled = false;
    });
  }, { passive: true });

  yearOutput.textContent = String(new Date().getFullYear());
})();
