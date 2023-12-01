import { useContext } from "react";
import { PredictContext } from "./PredictContext";

const usePredictContext = () => {
  const predict = useContext(PredictContext);
  return predict;
};

export default usePredictContext;
