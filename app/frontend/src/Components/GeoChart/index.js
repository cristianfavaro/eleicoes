import React, { useRef, useEffect, useState } from "react";
import { select, geoPath, geoMercator, json } from "d3";
import PopOver from "../PopOver";
import { Container, GeoChartContainer} from "./styles";
import Panel from "./Panel";
import Search from "./Search";

/**
 * Component that renders a map.
 * https://github.com/muratkemaldar/using-react-hooks-with-d3/blob/12-geo/src/GeoChart.js
 */

function joinFunc(features, data){
  return features
}




function Map({ urlData, hovered, setHovered, setGeojson, urlMap, colorScale, joinFunc, clicked, setClicked, headerField}) {
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
        console.log(clicked, ' vendo o clicked')
        console.log(feature, ' vendo o clicked')
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
        .attr("d", feature => pathGenerator(feature))  
        .attr("fill", feature => colorScale(feature, geojson))
        .attr("opacity", feature => feature.properties.data && `${feature.properties.data.c[0].pvap.replace(",", ".")}%`)
    }

    Promise.all([
      json(urlData),
      json(urlMap),
    ]).then(([data, geo]) => {    
      geo["features"] = joinFunc(geo.features, data)
      setGeojson(geo);
      createMap(geo);
    }).catch((e) => {
      console.error(e); // "oh, no!"
    })

  }, [urlMap, urlData, clicked]);

  return <Container ref={wrapperRef}> 
      
      <svg ref={svgRef}></svg>
      <PopOver headerField={headerField} properties={hovered && hovered.properties || undefined} />      
    </Container>  
};




const GeoChart = ({urlData, urlMap, colorScale, joinFunc, headerField}) => {
  const [hovered, setHovered] = useState(null);
  const [clicked, setClicked] = useState(null);
  const [geojson, setGeojson] = useState(false);

  return <GeoChartContainer>
    
    <div>
      <Search geojson={geojson} setClicked={setClicked}/>
      <Map {...{urlData, urlMap, setGeojson, colorScale, joinFunc, hovered, setHovered, clicked, setClicked, headerField}}/>
    </div>
    <Panel headerField={headerField} clicked={clicked}/>
  </GeoChartContainer>

}

GeoChart.defaultProps = {
  joinFunc: joinFunc,
  headerField: "cd",
  colorScale: ()=>{}
}
export default GeoChart;