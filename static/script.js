//const userid = document.getElementById('userid')
//const email = document.getElementById('email')
//const password = document.getElementById('password')
//const confirm_password = document.getElementById('confirm_password')
//const form = document.getElementById('form')
//const errorElement = document.getElementById('error')
//
//form.addEventListener('submit', (e) => {
//    let messages = []
//    if (email.value === '' || email.value == null) {
//        messages.push('Name is required')
//    }
//
//    if (password.value.length <= 6) {
//        messages.push('Password must be longer than 6 characters')
//    }
//    if (password.value.length >= 20) {
//        messages.push('Password must be less than 20 characters')
//    }
//
//    if (messages.length > 0) {
//        e.preventDefault()
//        errorElement.innerText = messages.join(', ')
//    }
//
//
//var check = function() {
//  if (document.getElementById('password').value ==
//    document.getElementById('confirm_password').value) {
//    document.getElementById('message').style.color = 'green';
//    document.getElementById('message').innerHTML = 'matching';
//  } else {
//    document.getElementById('message').style.color = 'red';
//    document.getElementById('message').innerHTML = 'not matching';
//  }
//}
//
//})

function validate(){
var emailid = document.getElementById("email").value;
var password = document.getElementById("password").value;
if ( emailid=="sanimabank@gmail.com" && password=="sanima123")
{
    alert("login successfully");
    window.location.replace("/index")
    return false;
}
else
{
    alert("Invalid Email or Password")
}
}