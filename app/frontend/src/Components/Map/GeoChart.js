import React, { useRef, useEffect, useState } from "react";
import { select, geoPath, geoMercator } from "d3";

/**
 * Component that renders a map.
 * https://github.com/muratkemaldar/using-react-hooks-with-d3/blob/12-geo/src/GeoChart.js
 */

import styled from 'styled-components';

const Container = styled.div`
  svg{
    z-index: -1;
  }
  span{
      background:#F8F8F8;
      border: 5px solid #DFDFDF;
      color: #717171;
      font-size: 13px;
      height: 30px;
      letter-spacing: 1px;
      line-height: 30px;
      position: relative;
      text-align: center;
      text-transform: uppercase;
      top: -80px;
      left:-30px;
      display:none;
      padding:0 20px;   
  }  
  span:after{
    content:'';
    position:absolute;
    bottom:-10px; 
    width:10px;
    height:10px;
    border-bottom:5px solid #dfdfdf;
    border-right:5px solid #dfdfdf;
    background:#f8f8f8;
    left:50%;
    margin-left:-10px;
    -moz-transform:rotate(45deg);
    -webkit-transform:rotate(45deg);
    transform:rotate(45deg);
  }
`

function GeoChart({ data, onClick, colorScale, onMouseOver=(d,i)=>{}}) {
  const svgRef = useRef();
  const wrapperRef = useRef();
  // const dimensions = useResizeObserver(wrapperRef);
  const [selected, setSelected] = useState(null);
  const [coordinates, setCoordinates] = useState(null);

  // will be called initially and on every data change
  useEffect(() => {
    const svg = select(svgRef.current);

    // use resized dimensions
    // but fall back to getBoundingClientRect, if no dimensions yet.
    const { width, height } = wrapperRef.current.getBoundingClientRect();
    // projects geo-coordinates on a 2D plane
    const projec = geoMercator()
      .fitSize([width, height], data) // assim fazia o zoom selected || data
      .precision(100);

    // takes geojson data,
    // transforms that into the d attribute of a path element
    const pathGenerator = geoPath().projection(projec);

    // Three function that change the tooltip when user hover / move / leave a cell
    var mouseover = function(event, feature) {
      setSelected(feature);  
      setCoordinates(event.target.getBoundingClientRect())
    }

    // render each country
    svg
      .selectAll(".country")
      .data(data.features)
      .join("path")
      .on("mouseover", mouseover)
      .attr("class", "country")
      .transition()
      .attr("fill", feature => colorScale(feature))
      .attr("d", feature => pathGenerator(feature))

  }, [data, colorScale]);

  useEffect(()=>{
    const svg = select(svgRef.current);
    // render text
    svg
      .selectAll(".label")
      .data([selected])
      .join("text")
      .attr("class", "label")
      .text(
        feature =>
          feature &&
          feature.properties.cd 
      )
      .attr("x", () => coordinates && coordinates["x"])
      .attr("y", () => coordinates && coordinates["y"]);

  }, [data, selected, coordinates])

  return (
    <Container ref={wrapperRef} style={{ marginBottom: "2rem" }}>
      <svg ref={svgRef}></svg>
    </Container>
  );
}

export default GeoChart;