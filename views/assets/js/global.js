const menuIcon = document.querySelector(".menu-icon");

menuIcon.addEventListener("click", () => {
	menuIcon.classList.toggle("click");
	menuIcon.classList.contains("click")
		? (document.querySelector("nav").style.zIndex = "10")
		: (document.querySelector("nav").style.zIndex = "-10");
});
