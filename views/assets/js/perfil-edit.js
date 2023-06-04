import "./global.js";

const btnSetImg = document.querySelector("img.edit-icon");
const avatarImg = document.querySelector("img#avatar");
const inputFile = document.querySelector("input#img");
const inputImg = document.querySelector("input#img_base64");

btnSetImg.addEventListener("click", () => {
	inputFile.click();
});

inputFile.addEventListener("change", () => {
	const image = inputFile.files[0];
	const reader = new FileReader();

	reader.addEventListener("load", () => {
		avatarImg.src = reader.result;
		inputImg.value = reader.result;
	});

	if (image) {
		reader.readAsDataURL(image);
	}
});
