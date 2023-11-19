import React, {useState} from 'react';

import GeoChart from './index';
// import countyData from "./Components/Map/data/counties.json";
// import stateData from "./Components/Map/data/states.json";

import geo from "./maps/br-estados.json";

function BrUFMap() {
  const colors = ["#B9EDDD", "#87CBB9", "#569DAA", "#577D86"];
  const [selectedCountry, setSelectedCountry] = useState(null);

  const colorScale = () => {
    return colors[Math.floor(Math.random() * 4)]
  };  
 
  return <div>
      <GeoChart 
          data=""
          geo={geo} 
          colorScale={colorScale}
          onMouseOver={(d,i)=>{console.log(d, i)}}
          selected={selectedCountry}
          onClick={ (event, feature) =>setSelectedCountry(selectedCountry === feature ? null : feature)} 
        />    
    </div>
}

export default BrUFMap;
