import React, {useState} from 'react';

import GeoChart from './Components/Map/GeoChart';
import "./App.css";

import { select, geoPath, geoAlbersUsa, geoMercator, min, max, scaleLinear, json } from "d3";
import data from "./Components/Map/data/GeoChart.world.geo.json";

// import countyData from "./Components/Map/data/counties.json";
// import stateData from "./Components/Map/data/states.json";
import brasilData from "./Components/Map/data/brasil.json";

const Map3 = () => {
  const colors = ["#B9EDDD", "#87CBB9", "#569DAA", "#577D86"];
  const [selectedCountry, setSelectedCountry] = useState(null);

  const [data, setData] = useState(null);

  // json("https://servicodados.ibge.gov.br/api/v3/malhas/paises/BR?formato=image/svg+xml&qualidade=minima&intrarregiao=UF").then(
  //   response => setData(response)
  // )

  const colorScale = (data) => {
    return colors[Math.floor(Math.random() * 4)]
  };
  
  return <GeoChart 
      data={brasilData} 
      colorScale={colorScale}
      onMouseOver={(d,i)=>{console.log(d, i)}}
      selected={selectedCountry}
      onClick={ (event, feature) =>setSelectedCountry(selectedCountry === feature ? null : feature)} 
    />
}

// const Map2 = () => {
//   const colors = ["#B9EDDD", "#87CBB9", "#569DAA", "#577D86"];
//   const [selectedCountry, setSelectedCountry] = useState(null);

//   const colorScale = (data) => {
//     return colors[Math.floor(Math.random() * 4)]
//   };

//   return <GeoChart 
//       data={countyData} 
//       projection={geoAlbersUsa}
//       colorScale={colorScale}
//       selected={selectedCountry}
//       onClick={ (event, feature) =>setSelectedCountry(selectedCountry === feature ? null : feature)} 
//     />
// }


function App() {

  const [selectedCountry, setSelectedCountry] = useState(null);
  const property = "pop_est";

  const minProp = min(data.features, feature => feature.properties[property]);
  const maxProp = max(data.features, feature => feature.properties[property]);
  
  const scale = scaleLinear()
      .domain([minProp, maxProp])
      .range(["#ccc", "red"]);

  const colorScale = (feature) => {
    return scale(feature.properties[property])
  } 

  return (
    <div className="App">
      <header className="App-header">
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        
        <Map3/>


        {/* <GeoChart 
          data={data} 
          colorScale={colorScale}
          selected={selectedCountry}
          onClick={ (event, feature) =>setSelectedCountry(selectedCountry === feature ? null : feature)} 
        /> */}

      </header>
    </div>
  );
}

export default App;
