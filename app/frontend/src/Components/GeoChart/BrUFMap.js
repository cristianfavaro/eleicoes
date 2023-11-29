import React, {useState} from 'react';
import GeoChart from './index';
import { colorPicker } from '../../utils/colorPicker';

function BrUFMap() {
  // const [selected, setSelected] = useState(null);

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
            data: data[ feature["properties"]["cd"] ] ? {
              ...data[ feature["properties"]["cd"] ],
              c: data[ feature["properties"]["cd"] ]["c"].sort(function(a,b){ //ordenando os candidatos desde aqui
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
          urlData="http://localhost:8080/eleicoes/544/br/states.json"
          urlMap="http://localhost:8080/maps/br-estados.json" 
          colorScale={colorScale}
          // selected={selected}
          joinFunc={joinFunc}
          // onClick={ (event, feature) =>setSelected(selected === feature ? null : feature)} 
        />    
    </div>
}

export default BrUFMap;
