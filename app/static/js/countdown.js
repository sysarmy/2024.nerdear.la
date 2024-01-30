"use strict";
/**
 * This code is used to get the remaining time till the start of the event.
 * The start of the event is in the deadlineDate
 */

const deadlineDate = "2023-09-26T09:00:00";
/**
 * This function gets the remaning time till the date parameter
 * @param {string} date The date which you want to get the remaining time
 * @returns  object with the unixTime, the days, the hours, the minutes, and the seconds till the date
 */
function getRemaningTime(date) {
	const unixTimeTillDeadline = Date.parse(date) - new Date();
	const days = Math.floor(unixTimeTillDeadline / 1000 / 60 / 60 / 24);
	const hours = Math.floor((unixTimeTillDeadline / 1000 / 60 / 60) % 24);
	const minutes = Math.floor((unixTimeTillDeadline / 1000 / 60) % 60);
	const seconds = Math.floor((unixTimeTillDeadline / 1000) % 60);
	return {
		unixTimeTillDeadline,
		days,
		hours,
		minutes,
		seconds,
	};
}

/**
 * This function sets the timer in the DOM and updates its value every 1 second
 * @param {string} selector The query selector to use
 * @param {string} date Deadline date which the timer counts for
 */
function setTimer(selector, date) {
	// Get the DOM for the countdown placeholders
	const timer = document.querySelector(selector);
	const days = timer.querySelector(".days");
	const hours = timer.querySelector(".hours");
	const minutes = timer.querySelector(".minutes");
	const seconds = timer.querySelector(".seconds");
	const timerTic = setInterval(updateTimer, 1000); // Set an interval

	updateTimer();
	/**
	 * This functions updates the DOM with the time until the deadlineDate
	 */
	function updateTimer() {
		const remainingTime = getRemaningTime(date);
		// Check if the deadline was completed to stop the timer
		if (remainingTime.unixTimeTillDeadline <= 0) {
			clearInterval(timerTic);
			// This set to 0 is done in case the user enters the event page after the deadline ended
			remainingTime.days = 0;
			remainingTime.hours = 0;
			remainingTime.minutes = 0;
			remainingTime.seconds = 0;
		}
		// If its not the case, updates the innerHTML to the remaning time
		days.innerHTML = getZero(remainingTime.days);
		hours.innerHTML = getZero(remainingTime.hours);
		minutes.innerHTML = getZero(remainingTime.minutes);
		seconds.innerHTML = getZero(remainingTime.seconds);
	}
	/**
	 * This function converts any number with 1 digit to a number with 2 digits
	 * @param {*} num
	 * @returns the number formatted for 2 digits
	 */
	function getZero(num) {
		if (num >= 0 && num < 10) {
			return "0" + num;
		} else {
			return num;
		}
	}
}

setTimer(".timer", deadlineDate);
