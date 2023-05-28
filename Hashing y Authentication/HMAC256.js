const crypto = require("crypto");

var algoritmo = "sha256";
var mensaje = "Hola chicos, como estáis?";
var key = "KeepCoding";

var hash = crypto.createHmac(algoritmo, key);

hash.update(mensaje);
console.log("Mensaje:\t", mensaje);
console.log("Clave:\t\t", key);
console.log("Método:\t\t", algoritmo);
var miHash = hash.digest("hex");
console.log("\nHMAC es:\t", miHash);
hash = crypto.createHash(algoritmo);
console.log("HMAC es:\t", hash.digest("base64"));
console.log("Longitud of HMAC: ", miHash.length * 4, " bits");
