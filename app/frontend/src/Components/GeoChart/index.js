import React, { useRef, useEffect, useState } from "react";
import { select, geoPath, geoMercator, json } from "d3";
import PopOver from "../PopOver";
import { Container } from "./styles";
import {apiEndPoints} from '../../utils/apiEndPoints';
/**
 * Component that renders a map.
 * https://github.com/muratkemaldar/using-react-hooks-with-d3/blob/12-geo/src/GeoChart.js
 */


function GeoChart({ data, geo, colorScale}) {
  const svgRef = useRef();
  const wrapperRef = useRef();
  // const dimensions = useResizeObserver(wrapperRef);
  const [selected, setSelected] = useState(null);
  
  // will be called initially and on every data change
  useEffect(() => {

    function createMap([data, geo]){
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
      var onMouseOver = function(event, feature){
        setSelected(feature)
      }
  
      var onMouseOut = function(e){
        setSelected(null)
      } 
  
      // render each place
      svg
        .selectAll(".place")
        .data(data.features)
        .join("path")
        .on("mouseover", onMouseOver)
        .on("mouseout", onMouseOut)
        .attr("class", "place")
        .transition()
        .attr("fill", feature => colorScale(feature))
        .attr("d", feature => pathGenerator(feature))  
    }

    Promise.all([
      // json(apiEndPoints.http + '/static/maps/br-estados.json/'),
      // json(COUNTIES),
    ]).then(() => {
      createMap([geo, []]);
    });

  }, [data, colorScale]);

  return <Container ref={wrapperRef}>
      <svg ref={svgRef}></svg>
      <PopOver data={selected} show={selected} />
    </Container>  
}

export default GeoChart;