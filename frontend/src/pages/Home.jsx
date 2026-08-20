import UploadSection from "../components/UploadSection";

function Home() {
    return(
        <div className = "app-shell">
            <header className = "app-header">
                    <h1>
                        InsightForge AI
                    </h1>
                    <p>
                        AI Business Intelligence Assistant
                    </p>
            </header>

            <main className = "dashboard-container">
                <section className = "dashboard-intro">
                    <h2>
                        Business Analytics Dashboard
                    </h2>
                    
                    <p>
                        Upload your CSV dataset to analyze data quality, KPIs, business insights, trends and customer behavior.
                    </p>

                </section>
                <UploadSection />
            </main>
            <footer className = "app-footer">
                InsightForge AI • Business Intelligence Assistant
            </footer>
        </div>
    );
}

export default Home;