var wordsList = [];

function init() {
  // Load the words from the dictionary text file to wordsList
  var wordsFile = "https://raw.githubusercontent.com/GirlsFirst/SIP-2017/master/Unit2_Applications/dictionary-attack/dictionary.txt?token=ADcVhZjRMd86ZdhPE2jVvIaJdQdzLA6Yks5YvvVSwA%3D%3D";
  $.get(wordsFile, function(data) {
    document.getElementById("btnSubmit").disabled = true;
	// Splits dictionary into a list of words
    wordsList = data.split('\n'); //everytime it sees a new line, it'll remove it and add it to the list
    document.getElementById("btnSubmit").disabled = false; 
  });
}

window.onload = init; //when the window loads, do the function init

/* ADD YOUR CODE BELOW */

//gets the password and converts all letters to lowercase "";

function checkPassword() {
	
	var pw = document.getElementById("pw").value.toLowerCase;
	var isSecure = true; //automatically assuming is secure
	var word ="";	
	
	//Check if the password is simililar to the dictionary words		
	//iterate over the list to see if password is contained
	for (var x = 0; x < wordsList.length; x++) {
		if (pw === words[x]) {			
			isSecure = false;
			word = wordsList[x];
			break;
		}
	}	
	printResult(isSecure, word);
}

//Print results of the password check 
function printResult(isSecure, word) {
	if (isSecure) {
		document.getElementById("results").innerHTML = word + " is secure!";
	else {
		document.getElementById("results").innerHTML = word + " not secure!";
}
