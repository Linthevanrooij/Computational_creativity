let yaml;
let grammar;
let firstSong, secondSong;
let words;
let functions;
let exclude = ["nigga", "niggas"];
let allLines = "Click To Generate";
let result = `
<start>: <line1> % <line2> % <line3> % <line4> % <line5>

<line1>: <jj>
<line2>: <nn> <vbz> | <nn> <vbd> | <nn> <vbg> | <nn> <vbn> | <nns> <vb> | <nns> <vbd> | <nns> <vbg> | <nns> <vbn>
<line3>: <pronoun1> <vbz> <jj> | <pronoun1> <vbd> <jj> | <pronoun1> <vbg> <jj> | <pronoun1> <vbn> <jj> | <pronoun2> <vb> <jj> | <pronoun2> <vbd> <jj> | <pronoun2> <vbg> <jj> | <pronoun2> <vbn> <jj> |<pronoun1> <vbz> <nn> | <pronoun1> <vbd> <nn> | <pronoun1> <vbg> <nn> | <pronoun1> <vbn> <nn> | <pronoun2> <vb> <nn> | <pronoun2> <vbd> <nn> | <pronoun2> <vbg> <nn> | <pronoun2> <vbn> <nn> | <pronoun1> <vbz> <nns> | <pronoun1> <vbd> <nns> | <pronoun1> <vbg> <nns> | <pronoun1> <vbn> <nns> | <pronoun2> <vb> <nns> | <pronoun2> <vbd> <nns> | <pronoun2> <vbg> <nns> | <pronoun2> <vbn> <nns>
<line4>: <i> <vb> <pronoun3> <jj> | <i> <vbd> <pronoun3> <jj> | <i> <vbn> <pronoun3> <jj> | <i> <vb> <pronoun3> <rb> | <i> <vbd> <pronoun3> <rb> | <i> <vbn> <pronoun3> <rb>
<line5>: <uh>

<pronoun1>: he | she | it
<pronoun2>: you | we | they
<pronoun3>: her | him | it
`
  ;

function preload() {
  // load lyrics
  firstSong = loadStrings('data/lightsPlease.txt');
  secondSong = loadStrings('data/noRoleModelz.txt');
  console.log(firstSong);
  console.log(secondSong);
}

function setup() {
  createCanvas(400, 200);
  textAlign(CENTER, CENTER);
  textSize(16);

  // make into one string
  let song1 = firstSong.join(' ');
  let song2 = secondSong.join(' ');
  songText = song1 + song2
  songText = songText.toLowerCase()
  words = songText.split(/([ ".,!,?])/);
  functions = RiTa.getPosTags(words);
  console.log(words)

  let dic = create_dict(functions, words);
  console.log(dic);


  // Create an array.
  for (let key in dic) {
    if (dic.hasOwnProperty(key) && key) { // Check if key is not empty
      result += `<${key}>: ${dic[key].join(' | ')}\n`;
    }
  }
  console.log(result);

  grammar = RiGrammar(result);


  // Save the text file.
  // saveStrings(result, 'data/first_grammar', '.txt');


}

function create_dict(functions, words) {
  let dictionary = { "vbg": [] }; // initialize with vbg 

  for (let i = 0; i < words.length; i++) {
    let func = functions[i];
    let word = words[i];
    const cleanWord = word.replace(/[?,"!@#$%^&*()_+=\-{}\[\];:<>]/g, '').trim();
    let cleanFunc = func.replace(/[?,"!@#$%^&*()_+=\-{}\[\];:<>]/g, '').trim();

    // If the function (key) doesn't exist, create an empty array
    if (!dictionary[cleanFunc]) {
      dictionary[cleanFunc] = [];
    }

    // if it is a word like diggin' place them in another category than noun
    if (cleanFunc == "nn" && cleanWord.endsWith("in'")) {
      cleanFunc = "vbg"
    }

    // push unique words
    if (!dictionary[cleanFunc].includes(cleanWord)) {
      if (!exclude.includes(word)) {
        dictionary[cleanFunc].push(cleanWord);
      }
    }


  }
  return dictionary

  // if we want something with concordance of words in the text
  // let params = {
  //   ignoreStopWords: true,
  //   ignoreCase: true,
  //   ignorePunctuation: true
  // };
  // let counts = RiTa.concordance(song.join(" "), params); 
}

function draw() {
  background(230, 240, 255);
  text(allLines, width / 2, height / 2);
  // frameRate(0.1);
}

function mouseReleased() {
  let elfje = grammar.expandFrom('<start>');
  let lines = elfje.split('%');
  allLines = lines.join('\n');
  console.log(allLines);
  // text(allLines, width / 2, height / 2);
}