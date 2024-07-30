





function printFunc(test : number) {
    if (test < 1) 
        return; 
    else { 
        console.log(test + " "); 
        printFunc(test - 1); // statement 2 
        console.log(test + " "); 
        return; 
    } 
}


// Driver code 
let testt = 3; 
printFunc(testt); 
