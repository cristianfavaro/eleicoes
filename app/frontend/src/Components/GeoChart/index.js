import React, { useRef, useEffect, useState } from "react";
import { select, geoPath, geoMercator, json } from "d3";
import PopOver from "../PopOver";
import { Container } from "./styles";
import Panel from "./Panel";
import { colorPicker } from '../../utils/colorPicker';

import styled from "styled-components";
import SubHeader from '../SubHeader';

/**
 * Component that renders a map.
 * https://github.com/muratkemaldar/using-react-hooks-with-d3/blob/12-geo/src/GeoChart.js
 */

const colorScale = (feature, clicked) => {  
  if(feature.properties.data){
    if(clicked){
      return clicked.properties.nm === feature.properties.nm ?
        colorPicker(feature.properties.data.c[0].p)
      : 
        "gray"
    }else{
      return colorPicker(feature.properties.data.c[0].p)
    }
  }else{
    return "white";
  };
};  

function joinFunc(features, data){
  return features
};

function Map({ hovered, setHovered, geojson, colorScale, clicked, setClicked}) {
  const svgRef = useRef();
  const wrapperRef = useRef();
  // const dimensions = useResizeObserver(wrapperRef);

  // will be called initially and on every data change
  useEffect(() => {
    function createMap(geojson){         
      const svg = select(svgRef.current);
      // use resized dimensions
      const { width, height } = wrapperRef.current.getBoundingClientRect();
      const projec = geoMercator()
        .fitSize([width, height], clicked || geojson) // assim fazia o zoom hovered || data
        .precision(100);
  
      // takes geojson data,
      // transforms that into the d attribute of a path element
      const pathGenerator = geoPath().projection(projec);
  
      // Three function that change the tooltip when user hover / move / leave a cell
      var onMouseOver = (event, feature) => {
        if(feature !== hovered){
          feature.properties.data && setHovered(feature);
        };
      };

      var onClick = (event, feature) => {
        setClicked(JSON.stringify(clicked) === JSON.stringify(feature)  ? null : feature);
      };

      var onMouseOut = e => setHovered(null)
          
      svg
        .selectAll(".place")
        .data(geojson.features)
        .join("path")
        .on("mouseover", onMouseOver)
        .on("mouseout", onMouseOut)
        .on("click", onClick)
        .attr("class", "place")       
        .transition()
        .attr("stroke", "#fff")
        .attr("stroke-width", "0.3px")
        .attr("d", feature => pathGenerator(feature))  
        .attr("fill", feature => colorScale(feature, clicked))
        .attr("opacity", feature => feature.properties.data && `${feature.properties.data.c[0].pvap.replace(",", ".")}%`)
    }

    geojson && createMap(geojson);

  }, [geojson, clicked]);

  return <Container ref={wrapperRef}> 
      <Back {...{clicked, setClicked}}/>
      <svg id="map" ref={svgRef}></svg>
    </Container>  
};


const GeoChart = ({urlData, urlMap, urlBrief, colorScale, joinFunc, titleComponent}) => {

  
  const [hovered, setHovered] = useState(null);
  const [clicked, setClicked] = useState(null);
  const [geojson, setGeojson] = useState(false);


  useEffect(()=>{
    Promise.all([
      json(urlBrief),
      json(urlMap),
    ]).then(([brief, geo]) => {    
      geo["features"] = joinFunc(geo.features, brief)
      setGeojson(geo);
    }).catch((e) => {
      console.error(e); // "oh, no!"
    })

  }, [urlMap, urlBrief])


  
  return <React.Fragment>
    <SubHeader {...{geojson, setClicked}}/>
    <Map {...{colorScale, geojson, hovered, setHovered, clicked, setClicked}}/>
    <Panel urlData={urlData} clicked={clicked} titleComponent={titleComponent}/>
    <PopOver titleComponent={titleComponent} hovered={hovered && hovered || undefined} />      
  </React.Fragment>
};



const Back = ({clicked, setClicked}) => {

  return clicked && <span
      onClick={()=>setClicked(null)}
    >
      {"< Voltar"}
    </span>
}


const TitleContainer = styled.div``
const TitleComponent = ({selected}) => {
  return <TitleContainer className="header">{selected && selected.properties["nm"]} </TitleContainer>
}

GeoChart.defaultProps = {
  joinFunc: joinFunc,
  colorScale: colorScale,
  titleComponent: TitleComponent,
}
export default GeoChart;