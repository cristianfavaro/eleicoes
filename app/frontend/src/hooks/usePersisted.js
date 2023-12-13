import {useState, useEffect, useReducer} from 'react';


function usePersistedState(key, initialState){
    const [state, setState] = useState(() => {
        const storageValue = localStorage.getItem(key);

        if(storageValue){
            return JSON.parse(storageValue)
        }else{
            return initialState;
        }
    });
    useEffect(() => {
        localStorage.setItem(key, JSON.stringify(state))
    }, [key, state]) 

    return [state, setState]
}


function usePersistedReducer(key, reducer, initialState){

    const start = () => {
        const storageValue = localStorage.getItem(key);

        if(storageValue){
            return JSON.parse(storageValue)
        }else{
            return initialState;
        }
    }

    const [state, dispatch] = useReducer(reducer, start());
    useEffect(() => {
        
        localStorage.setItem(key, JSON.stringify(state))
    
    }, [key, state]) 

    return [state, dispatch]
}


export {usePersistedState, usePersistedReducer}




