
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
        MDB	: "#79e7eb",
        PCdoB :  "#29c80a",
        PSB	:  "#a06f24",
        AGIR	: "#88101d",
        PMN	:  "#d98040",
        CIDADANIA	:  "#f52f7b",
        PV	: "#88121f",
        AVANTE	:  "#a4234e",
        PP	:  "#d7a7bc",
        PSTU	: "#e672d7",
        PCB	:  "#bde815",
        PRTB	:  "#552fc1",
        DC	: "#54baae",
        PCO	:  "#a659ad",
        PODE	:  "#8b62f0",
        PL	: "#0aa974",
        PSD	:  "#ec2594",
        SOLIDARIEDADE	:  "#a238e1",
        NOVO	: "#4487e7",
        REDE	:  "#a72732",
        PMB	:  "#ac9bd3",
        UP	: "#9858f1",
        UNIÃO	:  "#92de3b",
        PRD	:  "#176ae2",
    }

    return colors[party] ?? getRandomColor();
}