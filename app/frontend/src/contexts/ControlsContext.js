import React from 'react';
import {usePersistedState} from '../hooks/usePersisted';

const ControlsContext = React.createContext()


function ControlsProvider({children}){
    const [ele, setEle] = usePersistedState("ele", 544);
    
    return <ControlsContext.Provider value={{
                    ele, setEle
                }}
            >
                {children}
            </ControlsContext.Provider> 
}

export function useControls() {
    var context = React.useContext(ControlsContext);
    if(context === undefined){
      throw new Error("This hook must be used within a Header Provider");
    };
    return context;
};

export {ControlsProvider}