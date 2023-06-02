import "./global.js";

const pancsCarousel = document.querySelector(".pancs-carousel");
const pancControlPrev = pancsCarousel.querySelector(".control-prev");
const pancControlNext = pancsCarousel.querySelector(".control-next");
const pancsList = pancsCarousel.querySelector(".pancs-list");
const pancsItemCount = pancsList.childElementCount;

const recipesCarousel = document.querySelector(".recipes-carousel");
const recipeControlPrev = recipesCarousel.querySelector(".control-prev");
const recipeControlNext = recipesCarousel.querySelector(".control-next");
const recipesList = recipesCarousel.querySelector(".recipes-list");
const recipesItemCount = recipesList.childElementCount;

let currentPanc = 1;
pancControlPrev.addEventListener("click", () => {
	currentPanc--;
	if (currentPanc < 1) {
		currentPanc = pancsItemCount;
	}
	if (currentPanc === 1) {
		pancsList.style.transform = "translateX(0%)";
	} else {
		let value = (currentPanc - 1) * 248 + (currentPanc - 1) * 36;
		pancsList.style.transform = "translateX(-" + value + "px)";
	}
});
pancControlNext.addEventListener("click", () => {
	currentPanc++;
	if (currentPanc > pancsItemCount) {
		currentPanc = 1;
	}
	if (currentPanc !== 1) {
		let value = (currentPanc - 1) * 248 + (currentPanc - 1) * 36;
		pancsList.style.transform = "translateX(-" + value + "px)";
	} else {
		pancsList.style.transform = "translateX(0%)";
	}
});

let currentRecipe = 1;
recipeControlPrev.addEventListener("click", () => {
	currentRecipe--;
	if (currentRecipe < 1) {
		currentRecipe = recipesItemCount;
	}
	if (currentRecipe === 1) {
		recipesList.style.transform = "translateX(0%)";
	} else {
		let value = (currentRecipe - 1) * 248 + (currentRecipe - 1) * 36;
		recipesList.style.transform = "translateX(-" + value + "px)";
	}
});
recipeControlNext.addEventListener("click", () => {
	currentRecipe++;
	if (currentRecipe > recipesItemCount) {
		currentRecipe = 1;
	}
	if (currentRecipe !== 1) {
		let value = (currentRecipe - 1) * 248 + (currentRecipe - 1) * 36;
		recipesList.style.transform = "translateX(-" + value + "px)";
	} else {
		recipesList.style.transform = "translateX(0%)";
	}
});

const pancsItems = [...document.querySelectorAll(".panc-item")];

for (const pancItem of pancsItems) {
	pancItem.addEventListener("click", (ev) => {
		const origin = window.location.origin;
		window.location.href = origin + "/pancs/" + ev.currentTarget.id;
	});
}

const recipesItems = [...document.querySelectorAll(".recipe-item")];

for (const recipeItem of recipesItems) {
	recipeItem.addEventListener("click", (ev) => {
		const origin = window.location.origin;
		window.location.href = origin + "/receitas/" + ev.currentTarget.id;
	});
}
