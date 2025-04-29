const bodyE1 = document.querySelector("body")

bodyE1.addEventListener("mousemove",(event)=> {
    
    // Getting the value for mouse pointer in x and y axis
    const xPos = event.offsetX;
    const yPos = event.offsetY;

    // Creates a <span> element
    const spanE1 = document.createElement("span");

    // Sets the position of the <span>
    spanE1.style.left = xPos  + "px";
    spanE1.style.top = yPos+ "px";
    
    // Generates a random size for the <span>
    const size = Math.random()*100;
    spanE1.style.width = size+"px";
    spanE1.style.height = size+"px";

    // Appends the <span> to the document:
    bodyE1.appendChild(spanE1);

    // Removes the <span> after 3 seconds (3000 milliseconds):
    setTimeout(() => {spanE1.remove();},3000);
});

// Adding Functionality of the project

const containerE1 = document.querySelector(".container")

const careers = ["Youtuber","WebDeveloper","FreeLancer","Instructor"]

let careerIndex = 0;

let characterIndex = 0;

updateText()

function updateText(){

    characterIndex++;

    containerE1.innerHTML= `<h1> I am 
    
    ${careers[careerIndex].slice(0,1) === "I" ? "an": "a"} 
    
    ${careers[careerIndex].slice(0,characterIndex)} </h1>`;

    if(characterIndex === careers[careerIndex].length){
        careerIndex++;
        characterIndex = 0;
    }

    if(careerIndex === careers.length){
        careerIndex = 0;
    }
    setTimeout(updateText,100);



}

