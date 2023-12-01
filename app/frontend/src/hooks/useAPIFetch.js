import {useState, useEffect} from 'react';

// Função que joga para fora da API a responsabilidade de dar o fetch;
// Importante para usar com páginas que mudam conforme apenas o parâmetro URL;
export function useAPI(url, {method="GET", data={}, params={}} = {}){
    const [response, setResponse] = useState(false);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(false);
    
    async function fetchData(){
        setLoading(true);
        setError(false);
        await fetch({
            method: method, 
            url: url, 
            data: data,
            params: params, 
        })
        .then(response => setResponse(response))
        .catch(error => setError(error))
        setLoading(false);
    }

    return {response, loading, error, fetchData}
}


export function useAPIFetch(url, {method="GET", data={}, params={}} = {}){
    
    const {response, loading, error, fetchData} = useAPI(url, {method, data, params});
    useEffect( () => {        
        fetchData();
    }, [])

    return {response, loading, error}
}


