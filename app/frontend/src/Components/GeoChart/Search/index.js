import React from "react";
import AsyncSelect from 'react-select/async';

  
const Search = ({geojson, setClicked}) => {
    

    const filter = (inputValue) => {
        
        return geojson.features.filter((i) => 
          i.properties.cd.toLowerCase().includes(inputValue.toLowerCase())
        ).map(item => ({value: item.properties.cd, label: item.properties.cd, selected: item}));
      };
    
    const promiseOptions = (inputValue) =>
        new Promise((resolve) => {
        
            resolve(filter(inputValue));
        
    });
      
    return <div>
      
      <AsyncSelect 
        loadOptions={promiseOptions} 
        placeholder="Digite o nome da empresa ou código CVM"
        onChange={(e) => setClicked(e.selected)}
      />
  
    </div>
  }
  
export default Search;