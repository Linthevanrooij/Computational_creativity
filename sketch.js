let yaml, grammar;

function preload() {
  yaml = loadStrings('elfje_2.txt');
}

function setup() {
  createCanvas(400, 200);
  textAlign(CENTER, CENTER);
  textSize(16);

  grammar = new RiGrammar(yaml.join('\n'));
}

function draw() {
  background(220);

  // Generate elfje
  let elfje = grammar.expand().replaceAll("%", "\n");

  // Line layout
  let lines = elfje.split('\n');
  let allLines = lines.join('\n');  
  text(allLines, width / 2, height / 2);
  
  // split() > Splits a String into pieces and returns an array containing the pieces.
  // join() > Combines an array of strings into one string.

  frameRate(0.15);
}

