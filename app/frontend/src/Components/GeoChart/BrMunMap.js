import React from 'react';
import GeoChart from './index';

function BrMunMap() {
 
  function joinFunc(features, data){

    console.log(data, '  vendo a data agora')
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
          urlData="http://localhost:8080/eleicoes/544/br/br.json"
          urlBrief="http://localhost:8080/eleicoes/544/br/muns.json"
          urlMap="http://localhost:8080/maps/br-mun.json" 
          joinFunc={joinFunc}
        />    
    </div>
}

export default BrMunMap;
