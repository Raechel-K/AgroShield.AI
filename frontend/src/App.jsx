import { useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];

    if (!selectedFile) return;

    setFile(selectedFile);
    setPreview(URL.createObjectURL(selectedFile));
    setResult(null);
    setError("");
  };

  const analyzeLeaf = async () => {
    if (!file) {
      setError("Please select a leaf image first.");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error("Prediction request failed.");
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      console.error(err);
      setError(
        "Unable to connect to AgroShield AI. Make sure the backend server is running."
      );
    } finally {
      setLoading(false);
    }
  };

  const resetAnalysis = () => {
    setFile(null);
    setPreview(null);
    setResult(null);
    setError("");
  };

  return (
    <div className="app">
      <header className="navbar">
        <div className="logo">
          <span className="logo-icon">🌱</span>
          <span>AgroShield <b>AI</b></span>
        </div>

        <div className="nav-status">
          <span className="status-dot"></span>
          AI Model Online
        </div>
      </header>

      <main>
        <section className="hero">
          <div className="hero-content">
            <span className="badge">AI-POWERED CROP HEALTH</span>

            <h1>
              Protect Your Crops
              <br />
              <span>With Intelligent AI</span>
            </h1>

            <p>
              Upload a crop leaf image and AgroShield AI will analyze it
              using our trained machine-learning model to identify possible
              diseases.
            </p>
          </div>
        </section>

        <section className="analyzer">
          <div className="upload-card">
            <div className="section-title">
              <span>🔍</span>
              <div>
                <h2>Leaf Disease Analyzer</h2>
                <p>Upload a clear image of a crop leaf</p>
              </div>
            </div>

            {!preview ? (
              <label className="drop-zone">
                <div className="upload-icon">📷</div>

                <h3>Upload Leaf Image</h3>

                <p>
                  Click here to select an image from your computer
                </p>

                <span className="file-types">
                  JPG, JPEG or PNG
                </span>

                <input
                  type="file"
                  accept="image/jpeg,image/jpg,image/png"
                  onChange={handleFileChange}
                  hidden
                />
              </label>
            ) : (
              <div className="preview-area">
                <img
                  src={preview}
                  alt="Selected crop leaf"
                  className="leaf-preview"
                />

                <div className="file-name">
                  📄 {file?.name}
                </div>

                <button
                  className="change-button"
                  onClick={resetAnalysis}
                >
                  Choose Another Image
                </button>
              </div>
            )}

            {error && <div className="error">{error}</div>}

            <button
              className="analyze-button"
              onClick={analyzeLeaf}
              disabled={!file || loading}
            >
              {loading ? "🔄 Analyzing..." : "🔬 Analyze Leaf"}
            </button>
          </div>

          <div className="result-card">
            {!result && !loading && (
              <div className="empty-result">
                <div className="result-icon">🌿</div>
                <h2>Analysis Result</h2>
                <p>
                  Your AI prediction will appear here after
                  analyzing an image.
                </p>
              </div>
            )}

            {loading && (
              <div className="empty-result">
                <div className="loader"></div>
                <h2>Analyzing Leaf...</h2>
                <p>
                  AgroShield AI is examining the uploaded image.
                </p>
              </div>
            )}

            {result && (
              <div className="result">
                <div className="result-header">
                  <span>🤖</span>
                  <div>
                    <h2>Analysis Complete</h2>
                    <p>AgroShield AI prediction</p>
                  </div>
                </div>

                <div className="prediction-box">
                  <span className="label">Detected Condition</span>

                  <h3>
                    {result.disease
                      ?.replaceAll("___", " — ")
                      ?.replaceAll("__", " — ")
                      ?.replaceAll("_", " ")}
                  </h3>

                  <div className="confidence">
                    <div className="confidence-top">
                      <span>Confidence</span>
                      <strong>{result.confidence}%</strong>
                    </div>

                    <div className="progress">
                      <div
                        className="progress-bar"
                        style={{
                          width: `${Math.min(
                            Number(result.confidence),
                            100
                          )}%`,
                        }}
                      ></div>
                    </div>
                  </div>
                </div>

                <div className="information">
                  <h3>📋 Information</h3>
                  <p>
                    {result.information ||
                      "No additional information available."}
                  </p>
                </div>

                <button
                  className="new-analysis"
                  onClick={resetAnalysis}
                >
                  ↻ Analyze Another Leaf
                </button>
              </div>
            )}
          </div>
        </section>

        <section className="features">
          <div className="feature">
            <span>🤖</span>
            <div>
              <h3>AI Detection</h3>
              <p>Machine-learning powered disease identification.</p>
            </div>
          </div>

          <div className="feature">
            <span>⚡</span>
            <div>
              <h3>Fast Analysis</h3>
              <p>Get predictions within seconds.</p>
            </div>
          </div>

          <div className="feature">
            <span>🌾</span>
            <div>
              <h3>Multiple Crops</h3>
              <p>Supports maize, potato and tomato diseases.</p>
            </div>
          </div>
        </section>
      </main>

      <footer>
        <p>
          © 2026 <strong>AgroShield AI</strong> · Intelligent Agriculture
        </p>
      </footer>
    </div>
  );
}

export default App;