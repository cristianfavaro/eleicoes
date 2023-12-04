import React from "react";
import AsyncSelect from 'react-select/async';

  
const Search = ({geojson, setClicked}) => {
    
    const filter = (inputValue) => {
      return geojson.features
        .filter((i) => 
          i.properties.nm.toLowerCase().includes(inputValue.toLowerCase())
        ).map(item => ({value: item.properties.nm, label: item.properties.nm, selected: item}))
        .slice(0, 15);
    };
    
    const promiseOptions = (inputValue) =>
        new Promise((resolve) => {
        
            resolve(filter(inputValue));
        
    });
      
    return <AsyncSelect 
      isClearable
      loadOptions={promiseOptions} 
      placeholder="Digite o nome da localidade"
      onChange={ e => setClicked(e ? e.selected : null)}
    />

  }
  
export default Search;