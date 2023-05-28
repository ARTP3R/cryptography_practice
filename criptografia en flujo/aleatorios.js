//Generamos 8 bytes aleatorios con Nodejs

require("crypto").randomBytes(8, function (err, buffer) {
  var token = buffer.toString("hex");
  console.log(token);
});
