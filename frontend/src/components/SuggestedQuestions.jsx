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

        try {
            setLoading(true);
            setSelectedQuestion(question);
            setAnswer("");

            console.log("Sending question:", question);

            const response = await API.post(
                "/chat/",
                {
                    question: question.trim(),
                }
            );

            console.log("Full chat response:", response.data);

            let chatAnswer = response.data?.answer;

            /*
             * Handle backend/Gemini responses.
             *
             * Possible successful response:
             * {
             *   success: true,
             *   answer: "Chennai has the highest..."
             * }
             *
             * Possible quota error:
             * {
             *   success: false,
             *   error: {
             *      type: "quota_exceeded",
             *      message: "Gemini quota exceeded..."
             *   }
             * }
             */

            // ---------------------------------------
            // CASE 1: answer is an object
            // ---------------------------------------

            if (
                typeof chatAnswer === "object" &&
                chatAnswer !== null
            ) {
                // Gemini/API error
                if (
                    chatAnswer.success === false &&
                    chatAnswer.error
                ) {
                    chatAnswer =
                        `⚠️ **AI Service Unavailable**\n\n` +
                        `${chatAnswer.error.message || "Unable to get an AI response."}`;
                }

                // Normal successful object
                else if (chatAnswer.answer) {
                    chatAnswer = chatAnswer.answer;
                }

                // Unknown object
                else {
                    chatAnswer = JSON.stringify(
                        chatAnswer,
                        null,
                        2
                    );
                }
            }

            // ---------------------------------------
            // CASE 2: answer is a JSON string
            // ---------------------------------------

            if (typeof chatAnswer === "string") {
                try {
                    const parsed = JSON.parse(chatAnswer);

                    // Gemini/API error
                    if (
                        parsed?.success === false &&
                        parsed?.error
                    ) {
                        chatAnswer =
                            `⚠️ **AI Service Unavailable**\n\n` +
                            `${parsed.error.message || "Unable to get an AI response."}`;
                    }

                    // Successful JSON response
                    else if (parsed?.answer) {
                        chatAnswer = parsed.answer;
                    }
                } catch {
                    // Already normal text.
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
                    "⚠️ Unable to get an answer from the backend."
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

        if (!customQuestion.trim()) {
            return;
        }

        askQuestion(customQuestion);

        setCustomQuestion("");
    };

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
            {/* ================================= */}
            {/* Suggested Questions                */}
            {/* ================================= */}

            <h2>Suggested Questions</h2>

            <div>
                {questions &&
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
                    ))}
            </div>

            {/* ================================= */}
            {/* Ask Your Own Question              */}
            {/* ================================= */}

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
                            setCustomQuestion(
                                e.target.value
                            )
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
                        {loading
                            ? "Asking..."
                            : "Ask"}
                    </button>
                </form>
            </div>

            {/* ================================= */}
            {/* Loading                            */}
            {/* ================================= */}

            {loading && (
                <div
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
                        Analyzing your question...
                    </p>
                </div>
            )}

            {/* ================================= */}
            {/* AI Answer                         */}
            {/* ================================= */}

            {!loading && answer && (
                <div
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