import UploadSection from "../components/UploadSection";

function Home() {
    return(
        <div
            style = {{
                minHeight: "100vh",
                background: "#f5f7fb",
                color: "#1f2937",
                fontFamily: "Arial, Helvetica, sans-serif",
            }}
        >
            <header
                style={{
                    background: "#111827",
                    color: "white",
                    padding: "20px 40px",
                    boxShadow: "0 20px 8px rgba(0,0,0,0.08)",
                }}
            >
                <div
                    style={{
                        maxwidth: "1200px",
                        margin: "0 auto",
                    }}
                >
                    <h1
                        style={{
                            margin: 0,
                            fontSize: "28px",
                        }}    
                    >
                        InsightForge AI
                    </h1>
                    <p
                        style={{
                            margin: "6px 0 0",
                            color: "#d1d5db",
                            fontSize:"15px",
                        }}
                    >
                        AI Business Intelligence Assistant
                    </p>

                </div>
            </header>

            <main
                style={{
                    maxwidth: "1200px",
                    margin: "0 auto",
                    padding: "40px 20px",
                }}
            >
                <section
                    style = {{
                        marginBottom: "30px",
                    }}
                >
                    <h2
                        style={{
                            marginBottom: "80px",
                        }}
                    >
                        Business Analytics Dashboard
                    </h2>
                    
                    <p 
                        style={{
                            color: "#6b7280",
                            margin: 0,
                        }}
                    >
                        Upload your CSV dataset to analyze data quality, KPIs, business insights, trends and customer behavior.
                    </p>

                </section>
                <UploadSection />
            </main>
            <footer
                style={{
                    textAlign: "center",
                    padding: "25px",
                    color: "#6b7280",
                    fontSize: "14px",
                }}
            >
                InsightForge AI • Business Intelligence Assistant
            </footer>
        </div>
    );
}

export default Home;