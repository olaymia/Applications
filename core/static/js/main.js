
(function($){

	$.fn.calc = function( options) {

		return this.each(function(){

			var settings = $.extend({
				theme: 'default',
				borderRadius: ' '
			}, options);

			var $this = $(this);
			var $calcBtn = $this.find( '.calc-btn:not(.special)' );
			var $equals  = $this.find('.equals');
			var $del     = $this.find('.del');

			var $key = ' ';
			var keysPressed = [];
			var onScreen = $this.find('.screen');
			var res = ' ';

			$calcBtn.click(function(){
				$key = $(this).data('key') || $(this).html(); // set $key to the data attribute if defined if not set to inner HTML
				keysPressed.push($key);
				displayKeys();
			});

			$equals.click(function(){
				calculate(keysPressed);
			});

			$del.click(function(){
				// remove the last keyPressed and display on screen
				keysPressed.pop();
				displayKeys();
			});

			function displayKeys(){
				onScreen.val( keysPressed.join('') ); //take array and convert to string
			}

			function calculate(formula){
				var equation = formula.join('').replace(/[%]/g, "/100*"), // replace the % sign with the equation
				result = eval(equation);

				onScreen.val(result);
				keysPressed = [result]; //after calcuting empty the keysPressed and set new value
			}

			$this.addClass(settings.theme);

			$this.find('.calc-btn').css({
				'border-radius' : settings.borderRadius
			})
			

		});

	}

}(jQuery));

$('.calculator').calc({
	'theme' : 'dark'
});

$('.calculator2').calc({
	'borderRadius' : '10px'
});