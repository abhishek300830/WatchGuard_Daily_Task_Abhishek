let canvas = document.getElementById("canvas1");
let ctx = canvas.getContext("2d");

canvas.width = 800;
canvas.height = 800;

ctx.fillStyle = "#"+Math.floor(Math.random()*16777215).toString(16);
ctx.fillRect(10, 30, 200, 200);

ctx.lineWidth = 10;

ctx.strokeRect(10,250,200,200);

ctx.moveTo(10,500)
ctx.lineTo(200,700);
ctx.stroke();

ctx.beginPath()
ctx.arc(400,430,100,0,2*Math.PI)
ctx.stroke()