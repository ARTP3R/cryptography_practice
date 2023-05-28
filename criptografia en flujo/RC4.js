var crypto = require("crypto");

var password = "test";
var mensaje = "Hola chicos, vamos a aprender cripto en Keepcoding";

var key = crypto.createHash("sha256").update(password).digest();

//iv: sin contenido. Se concatena con la clave. Máximo 256 en total.
var cipher = crypto.createCipheriv("rc4", key, "");
var ciphertext = cipher.update(mensaje, "utf8", "hex");

console.log("Clave:\t", key.toString("hex"));
console.log("Texto Cifrado:\t", ciphertext);

var decipher = crypto.createDecipheriv("rc4", key, "");
var text = decipher.update(ciphertext, "hex", "utf8");
console.log("Texto plano:\t", text);
