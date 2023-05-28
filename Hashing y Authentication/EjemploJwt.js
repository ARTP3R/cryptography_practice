// npm install jwt-simple
var jwt = require("jwt-simple");

var key = "KeepCoding";
var pay = "{ foo: 'bar'}";

console.log("Mensaje a transmitir:\t", pay);
console.log("Password:\t", key);

var payload = pay;
var secret = key;

// codificar
var token = jwt.encode(payload, secret);
console.log("Token: ", token);

// decodificar
var decoded = jwt.decode(token, secret);
console.log("Payload: ", decoded);
