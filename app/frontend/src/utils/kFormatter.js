export function kFormatter(num) {
    return Math.abs(num) > 999999 ? 
        Math.sign(num)*((Math.abs(num)/1000000).toFixed(2)) + 'kk' 
    :   Math.abs(num) > 999 ? 
        Math.sign(num)*((Math.abs(num)/1000).toFixed(2)) + 'k' 
    :
        Math.sign(num)*Math.abs(num)
}


