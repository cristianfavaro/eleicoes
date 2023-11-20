
function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
};
  
export function colorPicker(party){
    const colors = {
        PT: "#cc2d2d",
        PSDB: "#3237d9",
        REPUBLICANOS: "#6b3ee6",
        PSOL: "#3237d9",
        PDT: "#f0b52e",
    }

    return colors[party] ?? getRandomColor();
}