const crypto = require("crypto");

var message = "Hola chicos, vamos a aprender cripto en Keepcoding";
var modulus = 1024;
var method = crypto.constants.RSA_PKCS1_OAEP_PADDING;
var padding = "RSA_PKCS1_OAEP_PADDING";


if (padding == "RSA_PKCS1_PADDING") method = crypto.constants.RSA_PKCS1_PADDING;
else if (padding == "RSA_PKCS1_OAEP_PADDING")
  method = crypto.constants.RSA_PKCS1_OAEP_PADDING;
else padding = crypto.constants.RSA_NO_PADDING;

const keyPair = crypto.generateKeyPairSync("rsa", {
  modulusLength: modulus,
  padding: method,
  publicKeyEncoding: { format: "pem", type: "spki" },
  privateKeyEncoding: { format: "pem", type: "pkcs8" },
});

encrypted = crypto.publicEncrypt(
  {
    key: keyPair.publicKey,
    padding: method,
    oaepHash: "sha256",
  },
  Buffer.from(message, "utf8")
);

var decrypted = crypto.privateDecrypt(
  {
    key: keyPair.privateKey,
    padding: method,
    oaepHash: "sha256",
    passphrase: "",
  },
  encrypted
);

console.log("Mensaje: ", message);
console.log("Padding:\t", padding);
console.log("Clave Privada:\n", keyPair.privateKey);
console.log("Clave Pública:\n", keyPair.publicKey);
console.log("Cifrado (hex): ", encrypted.toString("hex"));
console.log("Cifrado (b64): ", encrypted.toString("base64"));
console.log("\nDescifrado: ", decrypted.toString());
