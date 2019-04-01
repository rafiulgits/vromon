$(document).ready(function(){
	$('.spot-image-slider').slick({
		arrows: true,
		dots: true,
		infinite: true,
		speed: 300,
		slidesToShow: 1,
		adaptiveHeight: true,
		autoplay:true,
		autoplaySpeed:1000,
		centerMode: true,
		variableWidth: true,
	});
});