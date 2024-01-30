/**
 * This code queries the iframes and sets up loaders for each iframe element.
 */
document.addEventListener("DOMContentLoaded", function () {
	console.log("DOM LOADED");

	// Query the elements
	const iframeElements = document.getElementsByTagName("iframe");
	const loadingElements = document.getElementsByClassName("loading");

	// Iterate over each iframe element
	for (let i = 0; i < iframeElements.length; i++) {
		const iframe = iframeElements[i];
		const loading = loadingElements[i];

		console.log(`Adding load indicator to ${iframe.id}`);

		// Set an interval to add a dot to the loading indicator every second
		// setInterval(() => {
		// 	loading.textContent += ".";
		// }, 1000);

		// Add an event listener to the iframe's load event
		iframe.addEventListener("load", function () {
			console.log(`Finished loading ${iframe.id}`);

			// Hide the loading indicator
			loading.style.display = "none";
		});
	}
});
