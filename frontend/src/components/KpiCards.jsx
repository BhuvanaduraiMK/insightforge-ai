function KpiCards({ summary }) {
    return (
        <div
            style={{
                display: "flex",
                gap: "20px",
                flexWrap: "wrap",
                justifyContent: "center",
                marginTop: "20px",
            }}
        >
            <div style={cardStyle}>
                <h3>Rows</h3>
                <h1>{summary.rows}</h1>
            </div>

            <div style={cardStyle}>
                <h3>Columns</h3>
                <h1>{summary.columns}</h1>
            </div>

            <div style={cardStyle}>
                <h3>Health Score</h3>
                <h1>{summary.health_score}%</h1>
            </div>

            <div style={cardStyle}>
                <h3>Missing Values</h3>
                <h1>{summary.missing_values}</h1>
            </div>
        </div>
    );
}

const cardStyle = {
    width: "180px",
    padding: "20px",
    border: "1px solid #ddd",
    borderRadius: "10px",
    textAlign: "center",
    background: "#fafafa",
};

export default KpiCards;