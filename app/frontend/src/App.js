import React, {useState} from 'react';

import GeoChart from './Components/GeoChart';
// import countyData from "./Components/Map/data/counties.json";
// import stateData from "./Components/Map/data/states.json";
import brasilData from "./Components/Map/data/br-estados.json";

function App() {
  const colors = ["#B9EDDD", "#87CBB9", "#569DAA", "#577D86"];
  const [selectedCountry, setSelectedCountry] = useState(null);

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

export default App;
