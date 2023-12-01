import React, { useState } from "react";
import "./Home.css";
import ImageUploader from "./ImageUploader";
import ImageViewer from "./ImageViewer";
import PredictionResult from "./PredictionCard";

export default function Home() {
  const [image, setImage] = useState(null);

  return (
    <>
      <h2 className="text-center my-2">Chicken Disease Classification</h2>

      <div className="row my-4">
        <div className="col my-2 d-flex justify-content-md-center">
          <ImageViewer image={image} />
        </div>
      </div>
      <div className="row my-2 d-flex justify-content-md-center">
        <PredictionResult />
      </div>
      <div className="row my-2 ">
        <ImageUploader setImage={setImage} />
      </div>
    </>
  );
}
