import streamlit as st
import scipy.stats as stats

def perform_ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level=95):
    control_conversion_rate = control_conversions / control_visitors
    treatment_conversion_rate = treatment_conversions / treatment_visitors
    
    se_diff = ((control_conversion_rate * (1 - control_conversion_rate)) / control_visitors + 
               (treatment_conversion_rate * (1 - treatment_conversion_rate)) / treatment_visitors) ** 0.5
    
    observed_diff = treatment_conversion_rate - control_conversion_rate
    
    z_score = observed_diff / se_diff
    
    if confidence_level == 90:
        critical_z_value = stats.norm.ppf(0.95)
    elif confidence_level == 95:
        critical_z_value = stats.norm.ppf(0.975)
    elif confidence_level == 99:
        critical_z_value = stats.norm.ppf(0.995)
    else:
        raise ValueError("Invalid confidence level. Choose from 90, 95, or 99.")
    
    if z_score > critical_z_value:
        return "Treatment Group is Better"
    elif z_score < -critical_z_value:
        return "Control Group is Better"
    else:
        return "Indeterminate"


def main():
    st.markdown(
        """
        <style>
            body {
                background-image: url("dark-galaxy-milky-way-10.jpg");
                background-size: cover;
            }
            .input-container {
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
                margin-top: 100px;
            }
            .result-container {
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
                margin-top: 50px;
                opacity: 0;
                animation: slide-down 0.5s ease-in-out forwards;
            }
            @keyframes slide-down {
                0% { opacity: 0; transform: translateY(-50px); }
                100% { opacity: 1; transform: translateY(0); }
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("A/B Test Hypothesis Testing App")


    control_visitors = st.number_input("Control Group Visitors", min_value=0, step=1)
    control_conversions = st.number_input("Control Group Conversions", min_value=0, step=1)
    treatment_visitors = st.number_input("Treatment Group Visitors", min_value=0, step=1)
    treatment_conversions = st.number_input("Treatment Group Conversions", min_value=0, step=1)
    confidence_level = st.selectbox("Confidence Level", [90, 95, 99])

    if st.button("Perform Hypothesis Test"):
        result = perform_ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level)
        st.markdown(
            f"""
            <div class="result-container">
                <h2 style="color: blue;">Hypothesis Test Result:</h2>
                <p style="font-size: 20px;">{result}</p>
            </div>
            """,
            unsafe_allow_html=True
        )



if __name__ == "__main__":
    main()
