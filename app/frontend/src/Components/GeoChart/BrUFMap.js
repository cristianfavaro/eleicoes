import React, {useState} from 'react';

import GeoChart from './index';
// import countyData from "./Components/Map/data/counties.json";
// import stateData from "./Components/Map/data/states.json";

// import geo from "./maps/br-estados.json";

function BrUFMap() {
  const colors = ["#B9EDDD", "#87CBB9", "#569DAA", "#577D86"];
  const [selectedCountry, setSelectedCountry] = useState(null);

  const colorScale = (feature) => {
    return feature.properties.data ? colors[Math.floor(Math.random() * 4)] : "white"
  };  
 
  function joinFunc(features, data){
    return features.map(
      feature => {
        return {
          ...feature,
          properties: {
            ...feature["properties"], 
            data: data[0].states[feature["properties"]["cd"]]
          }
        }
      }
    )
  }


  return <div>
      <GeoChart 
          urlData="/api/eleicoes/544/br/"
          urlMap="http://localhost:8080/br-estados.json" 
          colorScale={colorScale}
          selected={selectedCountry}
          joinFunc={joinFunc}
          onClick={ (event, feature) =>setSelectedCountry(selectedCountry === feature ? null : feature)} 
        />    
    </div>
}

export default BrUFMap;
