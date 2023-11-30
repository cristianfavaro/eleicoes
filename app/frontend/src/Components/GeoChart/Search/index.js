import React from "react";
import AsyncSelect from 'react-select/async';


const colourOptions = [
    { value: 'ocean', label: 'Ocean', color: '#00B8D9', isFixed: true, test: "vendo se consigo mudar" },
    { value: 'blue', label: 'Blue', color: '#0052CC', isDisabled: true },
    { value: 'purple', label: 'Purple', color: '#5243AA' },
    { value: 'red', label: 'Red', color: '#FF5630', isFixed: true },
    { value: 'orange', label: 'Orange', color: '#FF8B00' },
    { value: 'yellow', label: 'Yellow', color: '#FFC400' },
    { value: 'green', label: 'Green', color: '#36B37E' },
    { value: 'forest', label: 'Forest', color: '#00875A' },
    { value: 'slate', label: 'Slate', color: '#253858' },
    { value: 'silver', label: 'Silver', color: '#666666' },
];

  
const Search = ({data}) => {

    const filter = (inputValue) => {
        return colourOptions.filter((i) =>
          i.label.toLowerCase().includes(inputValue.toLowerCase())
        );
      };
    
    const promiseOptions = (inputValue) =>
        new Promise((resolve) => {
        
            resolve(filter(inputValue));
        
    });
      
    return <div>
      
      <AsyncSelect 
         
        loadOptions={promiseOptions} 
        placeholder="Digite o nome da empresa ou código CVM"
        onChange={(e) => {console.log(e)}}
      />
  
    </div>
  }
  
export default Search;