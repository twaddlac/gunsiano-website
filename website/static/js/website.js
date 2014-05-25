$(document).ready(function() {
  drawWorm();
  homepageScrollEffects();
  togglePublications();
})

drawWorm = function() {
  var xStart = 131;
  var xEnd = 385;
  var yStart = 275;
  var radius = 5;
  var diameter = radius*2;

  var currentX = xStart;
  var currentY = yStart;
  var currentPosition = 0;
  var isForward = true;

  var canvas = document.getElementById("world-worms");
  if (canvas && canvas.getContext) {
    var context = canvas.getContext("2d");
    context.lineCap="round";
    context.lineWidth=3;
    setInterval(drawWorm, 200);
  }

  // Draws a worm with leftmost point [x, y]
  function drawWorm() {
    // arc(x, y, radius, startAngle, endAngle, anticlockwise);
    clearCanvas();
    context.beginPath();

    switch (currentPosition) {
      case 0:
        context.moveTo(currentX, currentY);
        context.arc(currentX + radius, currentY, radius, Math.PI, 0, false);

        context.moveTo(currentX + diameter, currentY);
        context.arc(currentX + diameter + radius, currentY, radius, Math.PI, 0, true);
        break;

      case 1:
        context.moveTo(currentX, currentY - radius);
        context.arc(currentX, currentY, radius, 3*Math.PI/2, 0, false);

        context.moveTo(currentX + radius, currentY);
        context.arc(currentX + diameter, currentY, radius, Math.PI, 0, true);

        context.moveTo(currentX + diameter + radius, currentY);
        context.arc(currentX + diameter*2, currentY, radius, Math.PI, 3*Math.PI/2, false);
        break;

      case 2:
        context.moveTo(currentX, currentY);
        context.arc(currentX + radius, currentY, radius, Math.PI, 0, true);

        context.moveTo(currentX + diameter, currentY);
        context.arc(currentX + diameter + radius, currentY, radius, Math.PI, 0, false);
        break;

      case 3:
        context.moveTo(currentX, currentY + radius);
        context.arc(currentX, currentY, radius, Math.PI/2, 0, true);

        context.moveTo(currentX + radius, currentY);
        context.arc(currentX + diameter, currentY, radius, Math.PI, 0, false);

        context.moveTo(currentX + (radius*3), currentY);
        context.arc(currentX + diameter*2, currentY, radius, Math.PI, Math.PI/2, true);
        break;
      default:
        break;
    }
    context.stroke();

    if (isForward) {
      currentX += radius;
      currentPosition = (currentPosition + 1) % 4;
      if (currentX > xEnd) {
        isForward = false;
      }
    } else {
      currentX -= radius;
      currentPosition -= 1;
      if (currentPosition <= -1) {
        currentPosition = 3;
      }
      if (currentX < xStart) {
        isForward = true;
      }
    }
  }

  function clearCanvas() {
    context.save(); // store current transformation matrix

    // Use the identity matrix while clearing the canvas
    context.setTransform(1, 0, 0, 1, 0, 0);
    context.clearRect(0, 0, canvas.width, canvas.height);

    context.restore(); // restore transform
  }
}

homepageScrollEffects = function() {
  if ($('body#home').length) {
    rotateMolecule();
    network.initialize();
    skrollr.init({
      smoothScrolling: false,
      forceHeight: false
    });
  }
}

var moleculeFrameHeight = 722;
var moleculeFrameWidth = 678;
var moleculeFrameCount = 20;

rotateMolecule = function() {
  var molecule = $("#rna-image");
  var step = 100 / moleculeFrameCount;

  var viewportHeight = $(window).height();
  var stepsInViewport = viewportHeight / step;

  var totalSteps = moleculeFrameCount + stepsInViewport;

  molecule.attr("data-bottom-top", "background-position:!0px 0px");

  var spritePosition;
  for (var i = 1; i < totalSteps; i++) {
    spritePosition = moleculeFrameWidth * i * -1;
    molecule.attr("data--" +  (step * i) + "p-bottom-top",
        "background-position:!" + spritePosition + "px 0px");
  }
}

network = {
  nodeRadius: 10,
  nodeColor: "yellow",
  edgeWidth: 3,
  edgeColor: "violet",
  numberOfNodes: 40,

  initialize: function() {
    this.canvas = $(".network-background-image");
    this.context = this.canvas.get(0).getContext("2d");
    this.context.canvas.width = this.canvas.width();
    this.context.canvas.height = this.canvas.height();

    this.getDimensions();
    this.context.fillStyle = this.nodeColor;
    for (i = 0; i < this.numberOfNodes; i++) {
      this.drawRandomNode();
    }
  },

  getDimensions: function() {
    this.width = this.canvas.width();
    this.height = this.canvas.height();
  },

  drawRandomNode: function() {
    var x = Math.floor(Math.random() * this.width);
    var y = Math.floor(Math.random() * this.height);
    this.context.beginPath();
    this.context.arc(x, y, this.nodeRadius, 0, 2*Math.PI);
    this.context.fill();
  }
}

togglePublications = function() {
  $("#pub-menu a").click(function() {
    // have only clicked menu item be active
    $("#pub-menu a").removeClass("active");
    $(this).addClass("active");

    // make counts and publications invisible
    $("#pub-count span").addClass("invisible");
    $(".publications").addClass("invisible");

    // make only the relevant count and publications display
    selector = $(this).attr("id");
    $("." + selector).removeClass("invisible");
  })
}
