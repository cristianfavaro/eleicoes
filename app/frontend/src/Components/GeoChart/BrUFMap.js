import React, {useState} from 'react';
import GeoChart from './index';
import {useControls} from '../../contexts/ControlsContext';

function BrUFMap() {
  const {ele} = useControls();
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

  return <GeoChart 
          urlBrief={`http://localhost:8080/eleicoes/${ele}/br/states.json`}
          urlData={`http://localhost:8080/eleicoes/${ele}/br/br.json`} 
          urlMap="http://localhost:8080/maps/br-estados.json" 
          joinFunc={joinFunc}
        />    
}

export default BrUFMap;
