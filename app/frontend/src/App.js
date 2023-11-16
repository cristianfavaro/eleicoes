import React, {useState} from 'react';
import Map from './Components/Map';

import GeoChart from './Components/Map/GeoChart';
import "./App.css";

import data from "./Components/Map/data/GeoChart.world.geo.json";

function App() {

  const [selectedCountry, setSelectedCountry] = useState(null);

  return (
    <div className="App">
      <header className="App-header">
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        
        <Map></Map>
        <GeoChart 
          data={data} 
          selected={selectedCountry}
          onClick={ (event, feature) =>setSelectedCountry(selectedCountry === feature ? null : feature)} 
          property={"pop_est"}
        />

      </header>
    </div>
  );
}

export default App;
