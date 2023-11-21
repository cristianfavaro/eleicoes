import React, { useRef, useEffect, useState } from "react";
import { select, geoPath, geoMercator, json } from "d3";
import PopOver from "../PopOver";
import { Container, GeoChartContainer} from "./styles";
import {apiEndPoints} from '../../utils/apiEndPoints';
import Panel from "./Panel";

/**
 * Component that renders a map.
 * https://github.com/muratkemaldar/using-react-hooks-with-d3/blob/12-geo/src/GeoChart.js
 */

function joinFunc(features, data){
  return features
}

function Map({ urlData, selected, setSelected, urlMap, colorScale, joinFunc, clicked, setClicked}) {
  const svgRef = useRef();
  const wrapperRef = useRef();
  // const dimensions = useResizeObserver(wrapperRef);
  
  // will be called initially and on every data change
  useEffect(() => {
    function createMap(data, geojson){         
      const svg = select(svgRef.current);
      // use resized dimensions
      
      const { width, height } = wrapperRef.current.getBoundingClientRect();
      
      const projec = geoMercator()
        .fitSize([width, height], geojson) // assim fazia o zoom selected || data
        .precision(100);
  
      // takes geojson data,
      // transforms that into the d attribute of a path element
      const pathGenerator = geoPath().projection(projec);
  
      // Three function that change the tooltip when user hover / move / leave a cell
      var onMouseOver = (event, feature) => {
        if(feature !== selected){
          feature.properties.data && setSelected(feature);
        };
      };
      var onClick = (event, feature) => {
        feature !== clicked && setClicked(feature);
      };
      var onMouseOut = e => setSelected(null)
          
      svg
        .selectAll(".place")
        .data(joinFunc(geojson.features, data))
        .join("path")
        .on("mouseover", onMouseOver)
        .on("mouseout", onMouseOut)
        .on("click", onClick)
        .attr("class", "place")       
        .transition()
        .attr("stroke", "black")
        .attr("d", feature => pathGenerator(feature))  
        .attr("fill", feature => colorScale(feature, data))
        .attr("opacity", feature => feature.properties.data && `${feature.properties.data.c[0].pvap.replace(",", ".")}%`)
    }

    Promise.all([
      json(apiEndPoints.http + urlData),
      json(urlMap),
    ]).then(([data, geojson]) => {    
      createMap(data, geojson);
    }).catch((e) => {
      console.error(e); // "oh, no!"
    })

  }, [urlMap, urlData]);

  return <Container ref={wrapperRef}>  
      <svg ref={svgRef}></svg>
      <PopOver properties={selected && selected.properties || undefined} />      
    </Container>  
};


const GeoChart = ({urlData, urlMap, colorScale, joinFunc}) => {
  const [selected, setSelected] = useState(null);
  const [clicked, setClicked] = useState(null)

  return <GeoChartContainer>
    <div>
      <Map {...{urlData, urlMap, colorScale, joinFunc, selected, setSelected, clicked, setClicked}}/>
    </div>
    <Panel clicked={clicked}/>
    

  </GeoChartContainer>
}

GeoChart.defaultProps = {
  joinFunc: joinFunc,
  colorScale: ()=>{}
}
export default GeoChart;