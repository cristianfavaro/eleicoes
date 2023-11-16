import React, { useRef, useEffect, useState } from "react";
import { select, geoPath, geoMercator, min, max, scaleLinear } from "d3";

/**
 * Component that renders a map.
 * https://github.com/muratkemaldar/using-react-hooks-with-d3/blob/12-geo/src/GeoChart.js
 */


function GeoChart({ data, selected, onClick, colorScale, onMouseOver=(d,i)=>{}, projection=geoMercator}) {
  const svgRef = useRef();
  const wrapperRef = useRef();
  // const dimensions = useResizeObserver(wrapperRef);
  
  // will be called initially and on every data change
  useEffect(() => {
    const svg = select(svgRef.current);

    // use resized dimensions
    // but fall back to getBoundingClientRect, if no dimensions yet.
    const { width, height } = wrapperRef.current.getBoundingClientRect();
    // projects geo-coordinates on a 2D plane
    const projec = projection()
      .fitSize([width, height], selected || data)
      .precision(100);

    // takes geojson data,
    // transforms that into the d attribute of a path element
    const pathGenerator = geoPath().projection(projec);

    // render each country
    svg
      .selectAll(".country")
      .data(data.features)
      .join("path")
      .on("click", onClick)
      .on('mouseover', onMouseOver)
      .on('mouseout', function (d, i){})
      .attr("class", "country")
      .transition()
      .attr("fill", feature => colorScale(feature))
      .attr("d", feature => pathGenerator(feature));

    // render text
    // svg
    //   .selectAll(".label")
    //   .data([selected])
    //   .join("text")
    //   .attr("class", "label")
    //   .text(
    //     feature =>
    //       feature &&
    //       feature.properties.name +
    //         ": " +
    //         feature.properties[property].toLocaleString()
    //   )
    //   .attr("x", 10)
    //   .attr("y", 25);

  }, [data, selected]);

  return (
    <div ref={wrapperRef} style={{ marginBottom: "2rem" }}>
      <svg ref={svgRef}></svg>
    </div>
  );
}

export default GeoChart;