import { useState } from "react";
import API from "../services/api";
import ReactMarkdown from "react-markdown";

function UploadSection() {
    const [file, setFile] = useState(null);
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);

    const uploadFile = async () => {
        if (!file) {
            alert("Please select a CSV file.");
            return;
        }

        const formData = new FormData();

        formData.append("file", file);
        formData.append(
            "question",
            "Summarize this dataset."
        );

        try {
            setLoading(true);

            const response = await API.post(
                "/upload/",
                formData,
                {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    },
                }
            );

            console.log(response.data);
            setResult(response.data);
        } catch (error) {
            console.error("Upload Error:", error);

            if (error.response) {
                console.log(error.response.data);
                alert(error.response.data.detail || "Backend Error");
            } else {
                alert(error.message);
            }
        } finally {
            setLoading(false);
        }
    };

    return (
        <div style={{ padding: "20px" }}>
            <h2>Upload Dataset</h2>

            <input
                type="file"
                accept=".csv"
                onChange={(e) => setFile(e.target.files[0])}
            />

            <br />
            <br />

            <button
                onClick={uploadFile}
                disabled={loading}
                style={{
                    padding: "10px 20px",
                    cursor: loading ? "not-allowed" : "pointer",
                }}
            >
                {loading ? "Analyzing..." : "Upload"}
            </button>

            {result && (
                <>
                    {/* Dataset Summary */}

                    <div
                        style={{
                            marginTop: "30px",
                            padding: "20px",
                            border: "1px solid #ddd",
                            borderRadius: "10px",
                            background: "#ffffff",
                        }}
                    >
                        <h2>Dataset Summary</h2>

                        <p>
                            <strong>File:</strong>{" "}
                            {result.filename}
                        </p>

                        <p>
                            <strong>Rows:</strong>{" "}
                            {result.dashboard.summary_cards.rows}
                        </p>

                        <p>
                            <strong>Columns:</strong>{" "}
                            {result.dashboard.summary_cards.columns}
                        </p>

                        <p>
                            <strong>Health Score:</strong>{" "}
                            {result.dashboard.summary_cards.health_score}%
                        </p>
                    </div>

                    {/* Executive Summary */}

                    <div
                        style={{
                            marginTop: "20px",
                            padding: "20px",
                            border: "1px solid #ddd",
                            borderRadius: "10px",
                            background: "#fafafa",
                        }}
                    >
                        <h2>Executive Summary</h2>

                        {result.answer.success ? (
                                <ReactMarkdown>
                                    {result.answer.answer}
                                </ReactMarkdown>
                            ) : (
                                <p style={{ color: "red" }}>
                                    {result.answer.error.message}
                                </p>
                        )}
                    </div>
                </>
            )}
        </div>
    );
}

export default UploadSection;