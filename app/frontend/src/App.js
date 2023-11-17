import React, {useState} from 'react';

import GeoChart from './Components/GeoChart';
import PopOver from './Components/PopOver';
// import countyData from "./Components/Map/data/counties.json";
// import stateData from "./Components/Map/data/states.json";
import brasilData from "./Components/Map/data/br-estados.json";

// for (let index = 0; index < brasilData["features"].length; index++) { 
  
//   brasilData["features"][index]["properties"] = {
//     ...brasilData["features"][index]["properties"],
//     "cd": estados[brasilData["features"][index]["properties"]["codarea"]]["sigla"],
//   } 
// }

const Map3 = () => {
  const colors = ["#B9EDDD", "#87CBB9", "#569DAA", "#577D86"];
  const [selectedCountry, setSelectedCountry] = useState(null);

  // json("https://servicodados.ibge.gov.br/api/v3/malhas/paises/BR?formato=image/svg+xml&qualidade=minima&intrarregiao=UF").then(
  //   response => setData(response)
  // )

  const colorScale = () => {
    return colors[Math.floor(Math.random() * 4)]
  };
  
  return <div>
    <GeoChart 
      data={brasilData} 
      colorScale={colorScale}
      onMouseOver={(d,i)=>{console.log(d, i)}}
      selected={selectedCountry}
      onClick={ (event, feature) =>setSelectedCountry(selectedCountry === feature ? null : feature)} 
    />
    </div>
}

function App() {
  return (
    <div>
      
      <Map3/>

    </div>
  );
}

export default App;
