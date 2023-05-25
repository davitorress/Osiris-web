const btnEdit = document.querySelector(".info button");

btnEdit.addEventListener("click", () => {
	const origin = window.location.origin;
	window.location.href = origin + "/perfil/editar";
});

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

const createdCarousel = document.querySelector(".created-carousel");
const createdControlPrev = createdCarousel.querySelector(".control-prev");
const createdControlNext = createdCarousel.querySelector(".control-next");
const createdList = createdCarousel.querySelector(".created-list");
const createdItemCount = createdList.childElementCount;

let currentPanc = 1;
pancControlPrev.addEventListener("click", () => {
	currentPanc--;
	if (currentPanc < 1) {
		currentPanc = pancsItemCount;
	}
	if (currentPanc === 1) {
		pancsList.style.transform = "translateX(0%)";
	} else {
		let value = (currentPanc - 1) * 184 + (currentPanc - 1) * 24;
		pancsList.style.transform = "translateX(-" + value + "px)";
	}
});
pancControlNext.addEventListener("click", () => {
	currentPanc++;
	if (currentPanc > pancsItemCount) {
		currentPanc = 1;
	}
	if (currentPanc !== 1) {
		let value = (currentPanc - 1) * 184 + (currentPanc - 1) * 24;
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
		let value = (currentRecipe - 1) * 184 + (currentRecipe - 1) * 24;
		recipesList.style.transform = "translateX(-" + value + "px)";
	}
});
recipeControlNext.addEventListener("click", () => {
	currentRecipe++;
	if (currentRecipe > recipesItemCount) {
		currentRecipe = 1;
	}
	if (currentRecipe !== 1) {
		let value = (currentRecipe - 1) * 184 + (currentRecipe - 1) * 24;
		recipesList.style.transform = "translateX(-" + value + "px)";
	} else {
		recipesList.style.transform = "translateX(0%)";
	}
});

let currentCreated = 1;
createdControlPrev.addEventListener("click", () => {
	currentCreated--;
	if (currentCreated < 1) {
		currentCreated = createdItemCount;
	}
	if (currentCreated === 1) {
		createdList.style.transform = "translateX(0%)";
	} else {
		let value = (currentCreated - 1) * 184 + (currentCreated - 1) * 24;
		createdList.style.transform = "translateX(-" + value + "px)";
	}
});
createdControlNext.addEventListener("click", () => {
	currentCreated++;
	if (currentCreated > createdItemCount) {
		currentCreated = 1;
	}
	if (currentCreated !== 1) {
		let value = (currentCreated - 1) * 184 + (currentCreated - 1) * 24;
		createdList.style.transform = "translateX(-" + value + "px)";
	} else {
		createdList.style.transform = "translateX(0%)";
	}
});
