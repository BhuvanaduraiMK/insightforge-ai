import { useState } from "react";
import API from "../services/api";
//import ReactMarkdown from "react-markdown";
import KpiCards from "./KpiCards";
import BusinessInsights from "./BusinessInsights";
import SuggestedQuestions from "./SuggestedQuestions";


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

            console.log("Upload response:", response.data);
            setResult(response.data);
        } catch (error) {
            console.error("Upload Error:", error);

            if (error.response) {
                console.log("Backend error:",error.response.data);
                alert(error.response.data?.detail || "Backend Error");
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

                        <KpiCards summary = {result.dashboard.summary_cards}/>

                        
                    </div>

                    <BusinessInsights
                        insights={result.dashboard.business_insights}
                    />
                    
                    {/* PDF Report */}
                    <div
                        style={{
                            marginTop:"20px",
                            padding:"20px",
                            border:"1px solid #ddd",
                            borderRadius: "10px",
                            background: "#ffffff",
                            textAlign: "center",
                        }}>
                        <h2>Business Report</h2>
                        
                        <p>
                            Your business analysis report has been generated successfully.
                        </p>

                        <a href={`http://127.0.0.1:8000/${result.pdf_report}`}
                            target="_blank" rel="noopener noreferrer"
                            style ={{
                                display:"inline-block",
                                padding: "12px 24px",
                                background: "#2563eb",
                                color:"white",
                                textDecoration: "none",
                                borderRadius: "8px",
                                fontWeight: "bold",
                            }}>
                                Download Business Report
                            </a>

                    </div>

                    <SuggestedQuestions
                    questions = {result.suggested_questions}
                    />
                </>
            )}
        </div>
    );
}

export default UploadSection;