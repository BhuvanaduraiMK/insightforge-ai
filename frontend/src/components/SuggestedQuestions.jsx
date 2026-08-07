function SuggestedQuestions({ questions }) {
    return (
        <div
            style={{
                marginTop: "30px",
                padding: "20px",
                border: "1px solid #ddd",
                borderRadius: "10px",
                background: "#fafafa",
            }}
        >
            <h2>Suggested Questions</h2>

            {questions.map((question, index) => (
                <button
                    key={index}
                    style={{
                        margin: "10px",
                        padding: "10px 15px",
                        cursor: "pointer",
                    }}
                >
                    {question}
                </button>
            ))}
        </div>
    );
}

export default SuggestedQuestions;