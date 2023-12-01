// import { } from 'react'

import Home from "./components/Home";
import PredictProvider from "./context/predict/PredictContext";

function App() {
  return (
    <>
      <PredictProvider>
        <div
          className="container-fluid my-4"
          // style={{
          //   backgroundColor: "#CAF0F8",
          //   borderRadius: "0.3rem",
          //   border: "1px solid #5E60CE",
          // }}
        >
          <Home />
        </div>
      </PredictProvider>
    </>
  );
}

export default App;
