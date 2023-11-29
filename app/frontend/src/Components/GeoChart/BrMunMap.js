import React from 'react';
import GeoChart from './index';
import { colorPicker } from '../../utils/colorPicker';

function BrMunMap() {
  const colorScale = (feature) => {
    return feature.properties.data ? colorPicker(feature.properties.data.c[0].p) : "white";
  };  
 
  function joinFunc(features, data){

    console.log(data, '  vendo a data agora')
    return features.map(
      feature => {
        return {
          ...feature,
          properties: {
            ...feature["properties"], 
            data: data[0].muns[ feature["properties"]["cd"] ] ? {
              ...data[0].muns[ feature["properties"]["cd"] ],
              c: data[0].muns[ feature["properties"]["cd"] ]["c"].sort(function(a,b){ //ordenando os candidatos desde aqui
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
          colorScale={colorScale}
          joinFunc={joinFunc}
          headerField="nm"
        />    
    </div>
}

export default BrMunMap;
