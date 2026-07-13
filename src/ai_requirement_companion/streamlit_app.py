import streamlit as st

from ai_requirement_companion.services.requirement_service import RequirementService

st.set_page_config(page_title="AI Requirement Companion", layout="wide")
st.title("AI Requirement Companion")
st.write("Analyze Software Requirements with AI Assistance from a QA Engineer's Perspective.")
requirement = st.text_area("Enter the software requirement to analyze:", height=300)
req_service=RequirementService()
if st.button("Analyze Requirement"):
    if requirement.strip():
        with st.spinner("Analyzing requirement..."):
            analysis_results = req_service.analyze(requirement)
            st.subheader("Analysis Results")
            st.markdown(analysis_results)
    else:
        st.warning("Please enter a software requirement to analyze.")
        st.stop()
    st.markdown(analysis_results)