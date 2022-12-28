const ret = require('fs');
const input = ret.readFileSync(0,'utf8').trim().split('\n');
 
let currentLine = 0;
function required(){
    return input[currentLine++];
}
 
let [M, N] = required().split(' ').map(x=>+x);
console.log(Math.floor(M*N/2));
