import styled from 'styled-components';


export const Container = styled.div`
    border: 1px solid lightgray;
    height: 80vh;
    overflow: auto;
    padding: 0.5rem 0.5rem 0 0.5rem;
    .header{
        position: sticky;
        display: flex;
        top: 0;
        justify-content: space-between;
        background-color: white;
        align-items: center;
    };
`

export const CandContainer = styled.div`
    display: flex;
    align-items: center;
    font-size: 0.5rem;
    
    border-bottom: 1px solid lightgray;
    
    b{
        font-size: 0.8rem;
    }
    img{
        height: 70px;
        border-radius: 100%;
    }
    >div{
        width: 100%;
    }
    .info{
        display: flex;
        width: 100%;
        justify-content: space-between;
        
        div{
            display: flex;
            flex-direction: column;
        }
        .data{
            >*{
                display: flex;
                justify-content: end;
            }
        }
    };
    .bar{
        height: 10px;
        background-color: lightgray;
        >div{
            height: 10px;
        }
    };
`
