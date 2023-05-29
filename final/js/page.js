let email = document.getElementById("email").value;
let product = document.getElementById("product").value;
let measurements = document.getElementById("measurements").value;
let moreInfo = document.getElementById("more-info").value;

let formHeader = document.getElementById("form-header");



function check(){
    email = document.getElementById("email").value;
    product = document.getElementById("product").value;
    measurements = document.getElementById("measurements").value;
    moreInfo = document.getElementById("more-info").value;

    if(email === "" || product === "" || measurements === "" || moreInfo === ""){
        alert("Please fill out all the information before submitting");
    }
    if(email != "" && product != "" && measurements != "" && moreInfo != ""){
        sendInfo();
    }



}
function sendInfo(){

    
    let quoteForm = document.getElementById("quote-form");
    let paragraph = document.getElementById("paragraph");
    let outputEmail = document.getElementById("output-email");
    let outputProduct = document.getElementById("output-product");
    let outputMeasurements = document.getElementById("output-measurements");
    let outputInfo = document.getElementById("output-info");

    quoteForm.innerHTML = "";
    formHeader.innerHTML = "";
    

    paragraph.innerHTML = "Your Information has Been Sent!";
    outputEmail.innerHTML = "Email: " + email;
    outputProduct.innerHTML = "Product: " + product;
    outputMeasurements.innerHTML = "Measurements: " + measurements;
    outputInfo.innerHTML = "Additional Information: " + moreInfo;


}



