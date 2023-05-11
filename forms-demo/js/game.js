// this file is for code needed for input, quiz and truth game 
//global variable for first name
//variable that can be used for all functions

//first name
let fname = "";

//function to get info from info
// check input, and produce a sentence

function greet(){
    let greetParagraph = document.getElementById("greet");
    
    //get the values from the form
    fname = document.getElementById("fname").value;
    let lname = document.getElementById("lname").value;
    let age = document.getElementById("age").value;

    // check the input 
    if (fname==="" || lname===""){
        alert("First and last name cannot be an empty string!")
        return;
    } 
    //age check 
    if (age==="" || age < 18){
        alert("Invalid age! You must be 18 or older")
        return;
    }

    //update the paragraphs
    greetParagraph.innerHTML= "Greetings!" + age + " year old " + fname + "!";

}

//function to play the trivia game

function trivia1(){
    //get handle to answer paragraph
    let triviaAnswer = document.getElementById("trivia-answer");

    let chocSelected = document.getElementById("chocolate").checked;
    let tunaSelected = document.getElementById("tuna").checked;
    let honeySelected = document.getElementById("honey").checked;

    //give the results
    if(chocSelected) {
        triviaAnswer.innerHTML = fname + " , chocoalte is wrong"
    }
    if(tunaSelected) {
        triviaAnswer.innerHTML = fname + " , tuna is wrong"
    }
    if(honeySelected) {
        triviaAnswer.innerHTML = fname + " , bravo you are correct"
    }
    else{
        triviaAnswer.innerHTML = fname + " , uh oh something went wrong"
    }

}

function twoTruthsAndALie(){
    let answer = document.getElementById("answer");

    let truth1Selected = document.getElementById("truth1").checked;
    let truth2Selected = document.getElementById("truth2").checked;
    let lieSelected = document.getElementById("lie").checked;

    if(truth1Selected){
        answer.innerHTML = fname + " , that is the wrong answer. Luckily I don't have allergies"
    }
    if(truth2Selected){
        answer.innerHTML = fname + " , that is the wrong answer. I loved eggs."
    }
    if(lieSelected){
        answer.innerHTML = fname + " , that is the right answer. I have never broken a bone."
    }

}