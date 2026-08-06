import { useState } from "react";
import API from "../services/api";

function UploadSection() {

    const [file, setFile] = useState(null);
    const [result, setResult] = useState(null);

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

            const response = await API.post(
                "/upload/",
                formData,
                {
                    headers: {
                        "Content-Type": "multipart/form-data"
                    }
                }
            );
            console.log(response.data);
            setResult(response.data);

            alert("Upload Successful!");

        }

        catch (error) {

            console.error("Upload Error:", error);
            if (error.response){
                console.log(error.response.data);
                alert(error.response.data.detail || "Backend Error");
            } else{
            alert(error.message);
            }
        }

    };

    return (
        <div>

            <h2>Upload Dataset</h2>

            <input
                type="file"
                accept=".csv"
                onChange={(e) => setFile(e.target.files[0])}
            />

            <br /><br />

            <button onClick={uploadFile}>
                Upload
            </button>
            {result && (
            <div style={{ marginTop: "30px" }}>
                <h2>AI Summary</h2>

                <p>{result.answer.answer}</p>
            </div>
            )}
            {result && (
                <div style={{ marginTop: "30px" }}>
                    <h2>Response</h2>

                    <pre>
                        {JSON.stringify(result, null, 2)}
                    </pre>
                </div>
            )}
        </div>

    );

}

export default UploadSection;