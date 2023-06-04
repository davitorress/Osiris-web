const menuIcon = document.querySelector(".menu-icon");

menuIcon.addEventListener("click", () => {
	menuIcon.classList.toggle("click");
	menuIcon.classList.contains("click")
		? (document.querySelector("nav").style.display = "block")
		: (document.querySelector("nav").style.display = "none");
});
