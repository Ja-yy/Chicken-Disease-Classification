import React, { createContext, useState, useMemo, useCallback } from "react";

export const PredictContext = createContext({});

const PredictProvider = (props) => {
  const host = "http://localhost:8001";

  const [result, setResult] = useState(null);

  const getPrediction = useCallback(
    async (imgFile) => {
      try {
        const formData = new FormData();
        formData.append("img", imgFile);
        const response = await fetch(`${host}/api/v1/predict/`, {
          method: "POST",
          body: formData,
        });

        if (!response.ok) {
          throw new Error("Network response was not ok");
        }

        const json = await response.json();
        setResult(json.prediction);
        return json;
      } catch (error) {
        console.error("Error:", error.message);
        // Handle errors
        return null;
      }
    },
    [host]
  );

  const contextValue = useMemo(
    () => ({ result, getPrediction }),
    [result, getPrediction]
  );

  return (
    <PredictContext.Provider value={contextValue}>
      {props.children}
    </PredictContext.Provider>
  );
};

export default PredictProvider;
