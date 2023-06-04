const btnSetImg = document.querySelector(".input-container button");
const inputFile = document.querySelector(".input-container input[type='file']");
const previewImg = document.querySelector(".input-container .input-container");
const inputImg = document.querySelector(".input-container #panc-img_base64");

btnSetImg.addEventListener("click", () => {
	inputFile.click();
});

inputFile.addEventListener("change", () => {
	const image = inputFile.files[0];
	const reader = new FileReader();

	reader.addEventListener("load", () => {
		previewImg.innerHTML = `
		<picture>
			<img src="${reader.result}" alt="" />
		</picture>
		<div class="rotate-icons">
			<img src="/assets/img/icons/rotate-right.svg" alt="rotate right" onclick='rotate()' />
			<img src="/assets/img/icons/rotate-left.svg" alt="rotate left" onclick='rotate()' />
		</div>
		`;
		inputImg.value = reader.result;
	});

	if (image) {
		reader.readAsDataURL(image);
	}
});

const pancDescription = document.querySelector("#panc-description");
const charCount = document.querySelector("p.char-counter span");
charCount.innerText = pancDescription.value.length;

pancDescription.addEventListener("keydown", (ev) => {
	if (pancDescription.value.length >= 240 && ev.key !== "Backspace") {
		ev.preventDefault();
	}
});
pancDescription.addEventListener("input", (ev) => {
	charCount.innerText = ev.currentTarget.value.length;
});

const addFarm = document.querySelector("#add-farm");
const removeFarm = document.querySelector("#remove-farm");
const fieldsFarm = document.querySelector(".fields-farm");

addFarm.addEventListener("click", () => {
	const textFarm = fieldsFarm.querySelector("textarea").cloneNode(true);
	textFarm.value = "";
	fieldsFarm.appendChild(textFarm);
});
removeFarm.addEventListener("click", () => {
	if (fieldsFarm.childElementCount > 1) {
		const child = [...fieldsFarm.querySelectorAll("textarea")][fieldsFarm.childElementCount - 1];
		fieldsFarm.removeChild(child);
	}
});
