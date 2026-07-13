import streamlit as st

from ai_requirement_companion.services.requirement_service import RequirementService


st.set_page_config(page_title="AI Requirement Companion", layout="wide")
st.title("AI Requirement Companion")
st.write("Analyze Software Requirements with AI Assistance from a QA Engineer's Perspective.")
requirement = st.text_area("Enter the software requirement to analyze:", height=300)
req_service=RequirementService()
if st.button("Analyze Requirement"):
    if not requirement.strip():
        st.warning("Please enter a software requirement to analyze.")
        st.stop()
    else:
        with st.spinner("Analyzing requirement..."):
            analysis = req_service.analyze(requirement)
            st.subheader("Requirement Summary")
            st.write(analysis.summary)
            for question in analysis.questions:
                st.write(question)
            for risk in analysis.risks:
                st.warning(risk)
            for test in analysis.positive_tests:
                st.success(test)
            # st.markdown(analysis.llm_response)
        