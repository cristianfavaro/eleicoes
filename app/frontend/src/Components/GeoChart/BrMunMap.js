import React, {useState} from 'react';
import GeoChart from './index';
import { colorPicker } from '../../utils/colorPicker';

function BrUFMap() {
  const [selectedCountry, setSelectedCountry] = useState(null);

  const colorScale = (feature) => {
    return feature.properties.data ? colorPicker(feature.properties.data.c[0].p) : "white";
  };  
 
  function joinFunc(features, data){
    return features.map(
      feature => {
        return {
          ...feature,
          properties: {
            ...feature["properties"], 
            data: data[0].states[ feature["properties"]["cd"] ] ? {
              ...data[0].states[ feature["properties"]["cd"] ],
              c: data[0].states[ feature["properties"]["cd"] ]["c"].sort(function(a,b){ //ordenando os candidatos desde aqui
                if(Number(a.vap) === Number(b.vap)){
                  return 0
                }else{
                  return Number(a.vap) < (b.vap) ? 1 : -1;
                }
              })               
            } : null
          }
        }
      }
    )
  };

  return <div>
      <GeoChart 
          urlData="/api/eleicoes/544/br/"
          urlMap="http://localhost:8080/br-mun.json" 
          // colorScale={colorScale}
          selected={selectedCountry}
          // joinFunc={joinFunc}
          // onClick={ (event, feature) =>setSelectedCountry(selectedCountry === feature ? null : feature)} 
        />    
    </div>
}

export default BrUFMap;
