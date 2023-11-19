const apiEndPoints = !process.env.NODE_ENV || process.env.NODE_ENV === "development" ?
    {
        ws: "ws://localhost:8000",
        http: "http://localhost:8000",
    }
    : {
        ws: "wss://cristianfavaro.com.br",
        http: "https://cristianfavaro.com.br",
    }

export {apiEndPoints}