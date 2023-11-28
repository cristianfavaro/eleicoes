import React from "react"
import { CircleProgressContainer } from "./styles"

const CircleProgress = ({value, color, title}) => {
    return <CircleProgressContainer
        value={value}
        color={color}
    >
      <div className="progress-bar-container">
        <div className="progress-bar css">
          <progress></progress>
        </div>
        <small>
          {title}
        </small>
      </div>
  
    </CircleProgressContainer>
}

CircleProgress.defaultProps = {
    title: "Urnas apuradas",
    value: 40, 
    color: "darkblue",
}

export default CircleProgress

