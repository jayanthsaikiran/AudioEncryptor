//http://localhost/Website/roxinehtml/roxine-package/html/index.html
//   var firebaseConfig = {
//     apiKey: "AIzaSyA-s4C8Tf7k2xartInfIpKBJxWCPCcjZic",
//     authDomain: "audio-encryptor.firebaseapp.com",
//     databaseURL: "https://audio-encryptor.firebaseio.com",
//     projectId: "audio-encryptor",
//     storageBucket: "",
//     messagingSenderId: "802830741670",
//     appId: "1:802830741670:web:6757a50ee16d12be310467"
//   };
//   // Initialize Firebase
//   firebase.initializeApp(firebaseConfig);

firebase.auth().onAuthStateChanged(function(user) {
    if (user){
        document.getElementById("google_button").innerHTML = "Logged in";
        document.getElementById("log_out").style.visibility="visibles";

    }
    else {
        document.getElementById("log_out").style.visibility="hidden";
        //Not signed in.
    }
});

function logOut() {
    firebase.auth().signOut().then(function() {
        console.log("Signout successful");
        // Sign-out successful.
      }).catch(function(error) {
        // An error happened.
      });
      
}


function login_google() {

    var provider = new firebase.auth.GoogleAuthProvider();
    console.log("reached");

    firebase.auth().signInWithPopup(provider).then(function(result) {
        // This gives you a Google Access Token. You can use it to access the Google API.
        var token = result.credential.accessToken;
        // The signed-in user info.
        var user = result.user;

        document.getElementById("google_button").innerHTML = "Logged in";
        // ...
      }).catch(function(error) {
        // Handle Errors here.
        var errorCode = error.code;
        var errorMessage = error.message;
        // The email of the user's account used.
        var email = error.email;
        // The firebase.auth.AuthCredential type that was used.
        var credential = error.credential;
        // ...
        console.log(errorCode);
      });
      
      
      

}