import React from "react";
import AsyncSelect from 'react-select/async';

  
const Search = ({geojson, setClicked}) => {
    
    const filter = (inputValue) => {
        
        return geojson.features.filter((i) => 
          i.properties.nm.toLowerCase().includes(inputValue.toLowerCase())
        ).map(item => ({value: item.properties.nm, label: item.properties.nm, selected: item}));
      };
    
    const promiseOptions = (inputValue) =>
        new Promise((resolve) => {
        
            resolve(filter(inputValue));
        
    });
      
    return <AsyncSelect 
      loadOptions={promiseOptions} 
      placeholder="Digite o nome da empresa ou código CVM"
      onChange={(e) => setClicked(e.selected)}
    />

  }
  
export default Search;