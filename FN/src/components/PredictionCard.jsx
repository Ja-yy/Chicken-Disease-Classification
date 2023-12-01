import React from "react";
import usePredictcontext from "../context/predict/UsePredictContext";

const PredictionSlider = () => {
  const { result } = usePredictcontext();

  const resultColorMap = {
    Healthy: {
      backgroundColor: "#95d5b2",
      border: "1px solid #2d6a4f",
      color: "#31572c",
    },
    Coccidiosis: {
      "background-color": "#fcb9b2",
      border: "1px solid #8c1c13",
      color: "#5e0b15",
    },
  };
  const textColor = resultColorMap[result];

  return (
    <>
      <div className="col-5 my-3">
        <div className="result-card">
          <h5>Predicted Result</h5>
          <div className="d-flex justify-content-center">
            <div className="result-pri-card" style={textColor}>
              {result ? result : "Upload Image to Predict"}
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default PredictionSlider;
