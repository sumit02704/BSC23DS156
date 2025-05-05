import streamlit as st
import hashlib
import time

# Function to create a new block
def create_block(index, data, previous_hash):
    return {
        "index": index,
        "data": data,
        "timestamp": time.time(),
        "previous_hash": previous_hash
    }

# Function to generate hash for a block
def generate_hash(block):
    block_string = f"{block['index']}{block['data']}{block['timestamp']}{block['previous_hash']}"
    return hashlib.sha256(block_string.encode()).hexdigest()

# Create the genesis block
def create_genesis_block():
    return create_block(0, "Genesis Block - School Ledger", "0")

# Initialize blockchain in session_state
if "blockchain" not in st.session_state:
    st.session_state.blockchain = [create_genesis_block()]

# Function to add a new student report block
def add_student_report(student_name, subject, grade):
    previous_block = st.session_state.blockchain[-1]
    new_index = previous_block["index"] + 1
    data = f"Student: {student_name}, Subject: {subject}, Grade: {grade}"
    previous_hash = generate_hash(previous_block)
    new_block = create_block(new_index, data, previous_hash)
    st.session_state.blockchain.append(new_block)

# Streamlit UI
st.title("📚 School Report Blockchain Ledger")

with st.form("student_form"):
    st.subheader("Add Student Report")
    student_name = st.text_input("Student Name")
    subject = st.text_input("Subject")
    grade = st.text_input("Grade")
    submitted = st.form_submit_button("Add Report")
    if submitted and student_name and subject and grade:
        add_student_report(student_name, subject, grade)
        st.success("✅ Report added to blockchain!")

st.subheader("📄 Blockchain Ledger")
for block in st.session_state.blockchain:
    st.write(f"**Block Index:** {block['index']}")
    st.write(f"**Data:** {block['data']}")
    st.write(f"**Timestamp:** {time.ctime(block['timestamp'])}")
    st.write(f"**Previous Hash:** `{block['previous_hash']}`")
    st.markdown("---")
