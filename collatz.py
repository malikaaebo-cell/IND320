import random
import streamlit as st

st.title("Collatz conjecture")

# Initialize session state
if "value" not in st.session_state:
    st.session_state.value = None
    st.session_state.started = False
    button_label = "Start"
elif st.session_state.value == 1:
    button_label = "Success!"
elif st.session_state.value % 2 == 0:
    button_label = "Half it"
else:
    button_label = "Triple and add one"

# Button label depends on state; knappen deaktiveres når målet er nådd
st.button(button_label, disabled=st.session_state.value == 1)
if st.session_state.value == 1:
    st.balloons()

# Output: viser verdien FRA FORRIGE runde, før neste steg regnes ut
if not st.session_state.started:
    st.write("Ready")
else:
    st.write(st.session_state.value)

# Oppdater tilstanden til neste rerun (dvs. neste knappetrykk)
# Kjøres IKKE videre når value == 1, slik at ingen "usett" verdi regnes ut i det stille
if not st.session_state.started:
    # Første trykk: trekk et tilfeldig tall og lagre det
    st.session_state.value = random.randint(1, 100)
    st.session_state.started = True
elif st.session_state.value != 1:
    if st.session_state.value % 2 == 0:
        st.session_state.value //= 2
    else:
        st.session_state.value = st.session_state.value * 3 + 1