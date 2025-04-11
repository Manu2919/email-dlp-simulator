import streamlit as st
from dlp_utils import apply_policy

st.set_page_config(page_title="Email DLP Policy Simulator", page_icon="📧")

st.title("📧 Email DLP Policy Simulator")
st.markdown("Simulate sending an email with DLP policy checks for sensitive data.")

with st.form("dlp_form"):
    to_email = st.text_input("To Email")
    subject = st.text_input("Subject")
    message = st.text_area("Message", height=200)
    submitted = st.form_submit_button("Send Email")

    if submitted:
        content = f"{subject}\n{message}"
        allowed, violations = apply_policy(to_email, content)

        if allowed:
            st.success("✅ Email sent successfully (simulation).")
        else:
            st.error("⛔ Email blocked due to policy violation(s):")
            for v in violations:
                st.warning(f"- {v}")
            # Log the blocked email
            with open("dlp_log.txt", "a") as log_file:
                log_file.write(f"Blocked Email to {to_email} | Violations: {violations}\n")
