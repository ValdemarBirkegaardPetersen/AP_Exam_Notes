let yvalues = [650];
let yvalues2 = [650];
let xspacing;
let amplitude, period, theta, dx;
let numerator;
function setup() {
	xspacing = 2;
	period = 215;
	theta = 0.0;
	amplitude = 50;
	dx = (TWO_PI / period) * xspacing;
	numerator = 0;

	createCanvas(650, 400);

	textSize(30);
	textAlign(CENTER, CENTER);
}

function draw() {
	background(225);
	calcWave(yvalues);
	renderWave(yvalues);
	text(yvalues[numerator],width/2-7,height/2+150);
	numerator++;
}


function calcWave (arr) {
	theta += 0.22;
	x = theta;

	for(let i = 0; i < 650; i++) {
		arr[i] = sin(x)*amplitude;
		x += dx;
	}
}

function renderWave(arr) {
	for (let i = 0; i < 650; i++) {
		stroke(0);
		strokeWeight(2);
		line(i*xspacing,200-arr[i]	,(i+1)*xspacing,200-arr[i + 1])
	}
}
