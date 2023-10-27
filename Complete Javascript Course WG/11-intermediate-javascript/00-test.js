

let forwordButton = document.getElementsByClassName("ud-btn ud-btn-small ud-btn-ghost ud-heading-sm control-bar-dropdown--trigger--iFz7P control-bar-dropdown--trigger-dark--1qTuU control-bar-dropdown--trigger-small--1ZPqx")[3]
let intervalID = setInterval(()=>{ forwordButton.click()},500)


// stop
clearInterval(intervalID)
