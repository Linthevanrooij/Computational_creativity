let SUBJECTS = ['COUNT', 'STRANGER', 'LOOK', 'CHURCH', 'CASTLE', 'PICTURE',
  'EYE', 'VILLAGE', 'TOWER', 'FARMER', 'WAY', 'GUEST', 'DAY',
  'HOUSE', 'TABLE', 'LABOURER'];
let PREDICATES = ['OPEN', 'SILENT', 'STRONG', 'GOOD', 'NARROW', 'NEAR',
    'NEW', 'QUIET', 'FAR', 'DEEP', 'LATE', 'DARK', 'FREE',
    'LARGE', 'OLD', 'ANGRY'];

let CONJUNCTIONS = [' AND ', ' OR ', ' THEREFORE ', '. ', '. ', '. ', '. ', '. '];

let OPERATORS = ['A', 'EVERY', 'NO', 'NOT EVERY'];

function generate_phrase() {
let text = random(OPERATORS) + ' ' + random(SUBJECTS);
if (text == 'A EYE') { text = 'AN EYE'; }
return text + ' IS ';
}

function generate_poem() {
return generate_phrase() +
random(PREDICATES) + random(CONJUNCTIONS) +
generate_phrase() + random(PREDICATES) + '.\n';
}

function setup() {
createCanvas(500, 40);
}

function draw() {
background(220);
text(generate_poem(), 10, 24);
frameRate(0.2);
}