import styled from 'styled-components';


export const Container = styled.div`
    border: 1px solid lightgray;
    height: 80vh;
    overflow: auto;
    grid-area: SB;
    padding: 0 0.5rem 0 0.5rem;
    
    .top-container{
        position: sticky;
        display: flex;
        top: 0;
        justify-content: space-between;
        background-color: white;
        align-items: center;
        padding: 0.5rem 0;
    };
    
    .header{
        display: block;
        font-weight: 600;
    }
`

export const CandContainer = styled.div`
    display: flex;
    align-items: center;
    font-size: 0.5rem;    
    border-bottom: 1px solid lightgray;
    b{
        font-size: 0.8rem;
    };
    img{
        width: 60px;
        margin: 0.5rem;
        /* clip-path: circle(); */
    };
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
