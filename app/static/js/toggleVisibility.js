function toggleVisibility(...querySelectors) {
	querySelectors.forEach((querySelector) => {
		let element = document.querySelector(querySelector);
		element.classList.toggle("d-none");
	});
}
