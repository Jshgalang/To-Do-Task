// $('.has-error').hide();
// $('input[name="text"]').on('keypress', function () {
// 	console.log('In keypress handler')
// 	$('.has-error').hide();
// });

var initialize = function () {
	// console.log('initialize called');
	$('input[name="text"]').on('keypress', function () {
	// console.log('In keypress handler');
	$('.has-error').hide();
	});
};
// console.log('list.js loaded');