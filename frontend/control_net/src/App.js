import React, { useState } from "react";
import axios from "axios";

const App = () => {
  const [sketchUrl, setSketchUrl] = useState(null);
  const [keywords, setKeywords] = useState([]);
  const [selectedKeyword, setSelectedKeyword] = useState("");
  const [message, setMessage] = useState("");

  const startGame = async () => {
    setMessage("");
    try {
      const response = await axios.post(
        "http://localhost:8000/sketch-image/start_game"
      );

      // setSketchUrl(response.data.sketch_url);
      // http://localhost:8000/sketch-image/?file_path=.%2Ftest_img%2Frandom_dog_image_edge.jpg

      const sketchResponse = await axios.get(
        "http://localhost:8000/sketch-image/",
        {
          params: {
            file_path: response.data.sketch_url,
          },
        }
      );

      setSketchUrl(sketchResponse.request.responseURL);

      setKeywords(response.data.keywords);
      setSelectedKeyword("");
    } catch (error) {
      console.error("Error starting game:", error);
      setSketchUrl(null);
    }
  };

  const handleKeywordChange = (e) => {
    setSelectedKeyword(e.target.value);
  };

  const submitGuess = () => {
    if (keywords.includes(selectedKeyword)) {
      const isCorrect =
        selectedKeyword.toLowerCase() ===
        sketchUrl.split("random_")[1].split("_")[0];
      if (isCorrect) {
        setMessage("Correct! Here is the original image.");
      } else {
        setMessage("Incorrect. Try again!");
      }
    } else {
      setMessage("Please select a valid keyword.");
    }
  };

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h1>Guess the Pixabay Image</h1>
      {!sketchUrl ? (
        <button onClick={startGame} style={{ padding: "10px 20px" }}>
          Start Game
        </button>
      ) : (
        <div>
          <h2>Guess the keyword for this image:</h2>
          <img
            src={sketchUrl}
            alt="Sketch from Pixabay"
            style={{ maxWidth: "100%", height: "auto" }}
          />
          <div>
            <select
              value={selectedKeyword}
              onChange={handleKeywordChange}
              style={{ padding: "10px", marginTop: "20px" }}
            >
              <option value="" disabled>
                Select a keyword
              </option>
              {keywords.map((keyword) => (
                <option key={keyword} value={keyword}>
                  {keyword}
                </option>
              ))}
            </select>
            <button
              onClick={submitGuess}
              style={{ padding: "10px 20px", marginLeft: "10px" }}
            >
              Submit Guess
            </button>
          </div>
          {message && <p>{message}</p>}
        </div>
      )}
    </div>
  );
};

export default App;
