import streamlit as st

from ai_requirement_companion.services.requirement_service import RequirementService
from dataclasses import asdict

def render_list(title: str, items: list[str]):
    st.subheader(title)
    if not items:
        st.info(f"No {title.lower()} were generated.")
        return
    for item in items:
        st.markdown(f"- {item}")


st.set_page_config(page_title="AI Requirement Companion", layout="wide")
show_debug = st.sidebar.checkbox("Show Debug Info", value=False)

st.title("AI Requirement Companion")
st.write("Analyze Software Requirements with AI Assistance from a QA Engineer's Perspective.")
requirement = st.text_area("Enter the software requirement to analyze:", height=300)
# Initialise the requirement service once.
requirement_service = RequirementService()

# ---------------------------------------------------------------------------
# Streamlit session state helpers
# ---------------------------------------------------------------------------
if "analysis" not in st.session_state:
    st.session_state.analysis = None

if st.button("Analyze Requirement"):
    if not requirement.strip():
        st.warning("Please enter a software requirement to analyze.")
        st.stop()
    with st.spinner("Analyzing requirement..."):
        analysis = requirement_service.analyze(requirement)
        st.session_state.analysis = analysis

# ---------------------------------------------------------------------------
# Render the results if we have an analysis stored in session state.
# This block runs on every script execution, independent of the debug
# checkbox state, ensuring the output is not cleared when the checkbox is
# toggled.
# ---------------------------------------------------------------------------
if st.session_state.analysis:
    analysis = st.session_state.analysis
    if show_debug:
        st.divider()
        st.subheader("Debug Info")
        st.markdown("### Raw LLM Response")
        st.code(analysis.raw_response, language="markdown")
        with st.expander("Parsed Object"):
            st.json(asdict(analysis))

    quality_score = requirement_service.calculate_quality_score(analysis)
    st.metric("Requirement Quality", f"{quality_score}/10")

    render_list("📋 Requirement Summary", [analysis.summary])
    render_list("❓ Questions for Product Owner", analysis.questions)
    render_list("⚠️ Ambiguities", analysis.ambiguities)
    render_list("⚠️ Risks", analysis.risks)
    render_list("✅ Positive Test Ideas", analysis.positive_tests)
    render_list("❌ Negative Test Ideas", analysis.negative_tests)
    render_list("📏 Boundary Test Ideas", analysis.boundary_tests)
    render_list("🔒 Security Test Ideas", analysis.security_tests)

            
        