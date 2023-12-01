import React from "react";

const ImageViewer = ({ image }) => {
  return (
    <div className={`img-container ${image ? "" : "hidden"}`}>
      {image && (
        <div className="d-flex justify-content-center">
          <img src={image} alt="uploaded" className="img-fluid img-preview" />
        </div>
      )}
    </div>
  );
};

export default ImageViewer;
