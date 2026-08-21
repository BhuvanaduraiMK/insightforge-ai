import { useState } from "react";
import API from "../services/api";
import ReactMarkdown from "react-markdown";

function SuggestedQuestions({ questions }) {
    const [answer, setAnswer] = useState("");
    const [loading, setLoading] = useState(false);
    const [selectedQuestion, setSelectedQuestion] = useState("");
    const [customQuestion, setCustomQuestion] = useState("");

    const askQuestion = async (question) => {
        if (!question || !question.trim()) {
            return;
        }

        const trimmedQuestion = question.trim();

        try {
            setLoading(true);
            setSelectedQuestion(trimmedQuestion);
            setAnswer("");

            console.log("Sending question:", trimmedQuestion);

            const response = await API.post("/chat/", {
                question: trimmedQuestion,
            });

            console.log("Full chat response:", response.data);


            const data = response.data;

            if (data?.success === false) {
                const errorMessage =
                    data?.error?.message ||
                    "Unable to generate an AI answer.";

                setAnswer(
                    `⚠️ **AI Service Unavailable**\n\n${errorMessage}`
                );

                return;
            }

        
            let chatAnswer = data?.answer;
        
            if (
                typeof chatAnswer === "object" &&
                chatAnswer !== null
            ) {
                if (chatAnswer.success === false) {
                    chatAnswer =
                        chatAnswer?.error?.message ||
                        "Unable to generate an AI answer.";
                } else if (chatAnswer.answer) {
                    chatAnswer = chatAnswer.answer;
                } else {
                    chatAnswer = JSON.stringify(
                        chatAnswer,
                        null,
                        2
                    );
                }
            }

            if (typeof chatAnswer === "string") {
                try {
                    const parsed = JSON.parse(chatAnswer);

                    if (
                        parsed?.success === false &&
                        parsed?.error
                    ) {
                        chatAnswer =
                            parsed.error.message ||
                            "Unable to generate an AI answer.";
                    } else if (parsed?.answer) {
                        chatAnswer = parsed.answer;
                    }
                } catch {
                    // Normal text 
                }
            }

            setAnswer(
                chatAnswer || "No answer received."
            );
        } catch (error) {
            console.error("Chat Error:", error);

            if (error.response) {
                console.error(
                    "Backend error:",
                    error.response.data
                );

                setAnswer(
                    error.response.data?.detail ||
                    error.response.data?.error?.message ||
                    "⚠️ Backend error occurred."
                );
            } else {
                setAnswer(
                    "⚠️ Unable to connect to the backend."
                );
            }
        } finally {
            setLoading(false);
        }
    };

    const handleCustomQuestion = (e) => {
        e.preventDefault();

        if (!customQuestion.trim() || loading) {
            return;
        }

        askQuestion(customQuestion);
        setCustomQuestion("");
    };

    return (
        <div
            className="light-panel"
            style={{
                marginTop: "30px",
                padding: "20px",
                border: "1px solid #d6b36a",
                borderRadius: "10px",
                background: "#f7f1e5",
            }}
        >

        

            <h2>Suggested Questions</h2>

            <div>
                {questions && questions.length > 0 ? (
                    questions.map((question, index) => (
                        <button
                            key={index}
                            onClick={() =>
                                askQuestion(question)
                            }
                            disabled={loading}
                            style={{
                                margin: "10px",
                                padding: "10px 15px",
                                cursor: loading
                                    ? "not-allowed"
                                    : "pointer",
                                borderRadius: "6px",
                                border: "1px solid #aaa",
                                background: "#ffffff",
                            }}
                        >
                            {question}
                        </button>
                    ))
                ) : (
                    <p>
                        No suggested questions available.
                    </p>
                )}
            </div>

            

            <div
                style={{
                    marginTop: "30px",
                    paddingTop: "20px",
                    borderTop: "1px solid #ddd",
                }}
            >
                <h2>Ask Your Own Question</h2>

                <form
                    onSubmit={handleCustomQuestion}
                    style={{
                        display: "flex",
                        gap: "10px",
                        alignItems: "center",
                    }}
                >
                    <input
                        type="text"
                        value={customQuestion}
                        onChange={(e) =>
                            setCustomQuestion(e.target.value)
                        }
                        placeholder="Ask anything about your dataset..."
                        disabled={loading}
                        style={{
                            flex: 1,
                            padding: "12px",
                            fontSize: "16px",
                            border: "1px solid #bbb",
                            borderRadius: "6px",
                            outline: "none",
                        }}
                    />

                    <button
                        type="submit"
                        disabled={
                            loading ||
                            !customQuestion.trim()
                        }
                        style={{
                            padding: "12px 20px",
                            fontSize: "16px",
                            borderRadius: "6px",
                            border: "none",
                            background: "#2563eb",
                            color: "white",
                            cursor:
                                loading ||
                                !customQuestion.trim()
                                    ? "not-allowed"
                                    : "pointer",
                        }}
                    >
                        {loading ? "Asking..." : "Ask"}
                    </button>
                </form>
            </div>

            

            {loading && (
                <div
                    className = "ai-answer"
                    style={{
                        marginTop: "20px",
                        padding: "20px",
                        border: "1px solid #d6b36a",
                        borderRadius: "10px",
                        background: "#ffffff",
                    }}
                >
                    <h3>AI Answer</h3>

                    <p>
                        Analyzing your question...
                    </p>
                </div>
            )}

            

            {!loading && answer && (
                <div
                    className="ai-answer"
                    style={{
                        marginTop: "20px",
                        padding: "20px",
                        border: "1px solid #ddd",
                        borderRadius: "10px",
                        background: "#ffffff",
                    }}
                >
                    <h3>AI Answer</h3>

                    <p>
                        <strong>
                            Question:
                        </strong>{" "}
                        {selectedQuestion}
                    </p>

                    <div
                        style={{
                            marginTop: "15px",
                            lineHeight: "1.7",
                        }}
                    >
                        <ReactMarkdown>
                            {answer}
                        </ReactMarkdown>
                    </div>
                </div>
            )}
        </div>
    );
}

export default SuggestedQuestions;