function BusinessInsights({ insights}) {
    return (
        <div
            style={{
                marginTop: "30px",
                padding: "20px",
                border: "1px solid #ddd",
                borderRadius: "10px",
                background: "#fafafa",
            }}>
            <h2>Business Insights</h2>
            <ul>
                {insights.map((item, index) => (
                    <li key={index} style={{marginBottom: "10px"}}>
                        {item}
                    </li>
                ))}
            </ul>

        </div>
    );
}

export default BusinessInsights;