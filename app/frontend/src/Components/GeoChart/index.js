import React, { useRef, useEffect, useState } from "react";
import { select, geoPath, geoMercator, json } from "d3";
import PopOver from "../PopOver";
import { Container } from "./styles";
import {apiEndPoints} from '../../utils/apiEndPoints';
/**
 * Component that renders a map.
 * https://github.com/muratkemaldar/using-react-hooks-with-d3/blob/12-geo/src/GeoChart.js
 */


function joinFunc(features, data){
  return features
}

function GeoChart({ urlData, urlMap, colorScale, joinFunc}) {
  const svgRef = useRef();
  const wrapperRef = useRef();
  // const dimensions = useResizeObserver(wrapperRef);
  const [selected, setSelected] = useState(null);
  
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
        console.log(feature)
        if(feature !== selected){
          feature.properties.data && setSelected(feature);
        } 
      }
      var onMouseOut = e => setSelected(null)
          
      svg
        .selectAll(".place")
        .data(joinFunc(geojson.features, data))
        .join("path")
        .on("mouseover", onMouseOver)
        .on("mouseout", onMouseOut)
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
    });

  }, [urlMap, urlData]);

  return <Container ref={wrapperRef}>
      <svg ref={svgRef}></svg>
      <PopOver properties={selected && selected.properties || undefined} />
      
    </Container>  
}

GeoChart.defaultProps = {
  joinFunc: joinFunc,
}
export default GeoChart;