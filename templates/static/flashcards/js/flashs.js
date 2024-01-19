function flip_card(i) {
    resp = document.getElementById(i).style;
    console.log(resp)
    if (document.getElementById(i).style.display == 'none') {
        console.log("veio pelo if")
        document.getElementById(i).style.display = 'block'  
    }
    else if (document.getElementById(i).style.display == 'block') {
        console.log("veio pelo else")
        document.getElementById(i).style.display = 'none'
    }
    else {
        document.getElementById(i).style.display = 'block'  
    }
}