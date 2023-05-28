//Conversiones UTF8 a Hexadecimal y UTF8 a b64

const string_hex = Buffer.from("Hola", "utf8").toString("hex");
console.log(string_hex);

const string_b64 = Buffer.from("KeepCoding mola mucho", "utf8").toString("base64");
console.log(string_b64);

const string_utf8 = Buffer.from("5050", "hex").toString("utf8");
console.log(string_utf8);