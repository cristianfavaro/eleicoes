
import styled from 'styled-components';

export const CircleProgressContainer = styled.div`
    /* https://nikitahl.com/circle-progress-bar-css */

    .progress-bar-container{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    

    @property --progress-value {
        syntax: '<integer>';
        inherits: false;
        initial-value: 0;
    };

    @keyframes css-progress {
        to { --progress-value: ${props => props.value}; }
    }

    .progress-bar {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        /* to center the percentage value */
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .progress-bar::before {
        counter-reset: percentage var(--progress-value);
        content: counter(percentage) '%';
    }

    .css {
    background: 
        radial-gradient(closest-side, white 79%, transparent 80% 100%, white 0),
        conic-gradient(${props=>props.color} calc(var(--progress-value) * 1%), #e2dede 0);
        animation: css-progress 2s 1 forwards;
    }

    .css::before {
        animation: css-progress 2s 1 forwards;
    }

    progress {
        visibility: hidden;
        width: 0;
        height: 0;
    };
    small{
        color: #7e7a7a;
        padding: 0.3rem;
    }

`