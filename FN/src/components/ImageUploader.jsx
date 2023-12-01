import { useRef, useState, useEffect } from "react";
import usePredictcontext from "../context/predict/UsePredictContext";

// eslint-disable-next-line react/prop-types
const ImageUploader = ({ setImage }) => {
  const fileInputRef = useRef(null);
  const { getPrediction } = usePredictcontext();

  const [imageData, setImageData] = useState(null);
  const [isBtnDisabled, setIsBtnDisabled] = useState(true);

  useEffect(() => {
    setIsBtnDisabled(!imageData);
  }, [imageData]);

  const handleImageUpload = async (e) => {
    const uploadedImage = e.target.files[0];
    setImageData(uploadedImage);
    setImage(URL.createObjectURL(uploadedImage));

    const reader = new FileReader();

    reader.onloadend = () => {
      // eslint-disable-next-line no-unused-vars
      const bytes = new Uint8Array(reader.result);
    };

    if (uploadedImage) {
      reader.readAsArrayBuffer(uploadedImage);
    }
  };

  const handleButtonClick = () => {
    if (fileInputRef.current) {
      fileInputRef.current.click();
    }
  };

  const handlePredictBtnClick = () => {
    if (imageData) {
      getPrediction(imageData);
    } else {
      console.error("No image selected!");
      // Handle case when no image is selected
    }
  };

  return (
    <div className="d-flex justify-content-center">
      <button
        type="button"
        className="bton bton-upl mx-3"
        onClick={handleButtonClick}
      >
        Upload Image
      </button>
      <input
        type="file"
        ref={fileInputRef}
        accept=".jpg, .jpeg, .png"
        onChange={handleImageUpload}
        style={{ display: "none" }}
      />

      <button
        type="button"
        disabled={isBtnDisabled}
        className="bton bton-pri"
        onClick={handlePredictBtnClick}
      >
        Predict
      </button>
    </div>
  );
};

export default ImageUploader;
