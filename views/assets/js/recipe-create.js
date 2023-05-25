const btnSetImg = document.querySelector(".input-container button");
const inputFile = document.querySelector(".input-container input[type='file']");
const previewImg = document.querySelector(".input-container .input-container");
const inputImg = document.querySelector(".input-container #recipe-img_base64");

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
			<img src="/assets/img/icons/rotate-right.svg" alt="rotate right" />
			<img src="/assets/img/icons/rotate-left.svg" alt="rotate left" />
		</div>
		`;
		inputImg.value = reader.result;
	});

	if (image) {
		reader.readAsDataURL(image);
	}
});

const addPanc = document.querySelector("#add-panc");
const removePanc = document.querySelector("#remove-panc");
const fieldsPanc = document.querySelector(".fields-panc");

addPanc.addEventListener("click", () => {
	const selectPanc = document.querySelector("select[name='recipe-pancs[]']").cloneNode(true);
	fieldsPanc.appendChild(selectPanc);
});
removePanc.addEventListener("click", () => {
	if (fieldsPanc.childElementCount > 1) {
		const child = [...fieldsPanc.querySelectorAll("select[name='recipe-pancs[]']")][fieldsPanc.childElementCount - 1];
		fieldsPanc.removeChild(child);
	}
});

const addIngredient = document.querySelector("#add-ingredient");
const removeIngredient = document.querySelector("#remove-ingredient");
const fieldsIngredient = document.querySelector(".fields-ingredient");

addIngredient.addEventListener("click", () => {
	const inputIngredient = document.querySelector("input[name='recipe-ingredients[]']").cloneNode(true);
	inputIngredient.value = "";
	fieldsIngredient.appendChild(inputIngredient);
});
removeIngredient.addEventListener("click", () => {
	if (fieldsIngredient.childElementCount > 1) {
		const child = [...fieldsIngredient.querySelectorAll("input[name='recipe-ingredients[]']")][
			fieldsIngredient.childElementCount - 1
		];
		fieldsIngredient.removeChild(child);
	}
});

const addPrepare = document.querySelector("#add-prepare");
const removePrepare = document.querySelector("#remove-prepare");
const fieldsPrepare = document.querySelector(".fields-prepare");

addPrepare.addEventListener("click", () => {
	const divPrepare = fieldsPrepare.querySelector("div").cloneNode(true);
	divPrepare.querySelector("span").innerText = fieldsPrepare.childElementCount + 1;
	divPrepare.querySelector("textarea").value = "";
	fieldsPrepare.appendChild(divPrepare);
});
removePrepare.addEventListener("click", () => {
	if (fieldsPrepare.childElementCount > 1) {
		const child = [...fieldsPrepare.querySelectorAll("div")][fieldsPrepare.childElementCount - 1];
		fieldsPrepare.removeChild(child);
	}
});
